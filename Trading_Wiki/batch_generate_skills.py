"""Batch generate skills for all 11 trading books using wiki + raw extracts."""
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

SKILLS_DIR = Path.home() / ".config" / "opencode" / "skills"
WIKI_DIR = Path(__file__).parent / "wiki"
RAW_DIR = Path(__file__).parent / "raw"
AUTO_DETECT = SKILLS_DIR / "book-to-skill-bridge" / "scripts" / "auto_detect.py"
EXTRACT_SCRIPT = SKILLS_DIR / "book-to-skill" / "scripts" / "extract.py"

BOOKS = [
    {
        "slug": "wyckoff-2-0",
        "pdf_subdir": "trading",
        "pdf_glob": "Wyckoff 2.0*[.]pdf",
        "wiki_articles": ["wyckoff-method-overview", "wyckoff-2-framework"],
        "title": "Wyckoff 2.0: Structures, Volume Profile and Order Flow",
        "author": "Rubén Villahermosa Chaves",
    },
    {
        "slug": "volume-price-analysis",
        "pdf_subdir": "trading",
        "pdf_glob": "A Complete Guide*[.]pdf",
        "wiki_articles": ["volume-price-analysis-vpa"],
        "title": "A Complete Guide to Volume Price Analysis",
        "author": "Anna Coulling",
    },
    {
        "slug": "volume-profile",
        "pdf_subdir": "trading",
        "pdf_glob": "VOLUME PROFILE*[.]pdf",
        "wiki_articles": ["volume-profile", "volume-at-price-vap"],
        "title": "Volume Profile: The Insider's Guide to Trading",
        "author": "Trader Dale",
    },
    {
        "slug": "trades-about-to-happen",
        "pdf_subdir": "trading",
        "pdf_glob": "Trades About*[.]pdf",
        "wiki_articles": ["tape-reading-wis-wave", "order-flow-footprint"],
        "title": "Trades About to Happen",
        "author": "David H. Weis",
    },
    {
        "slug": "trading-against-the-crowd",
        "pdf_subdir": "trading",
        "pdf_glob": "Trading Against*[.]pdf",
        "wiki_articles": ["contrarian-sentiment-analysis"],
        "title": "Trading Against the Crowd",
        "author": "John F. Summa",
    },
    {
        "slug": "price-action-volman",
        "pdf_subdir": "scalping-trading",
        "pdf_glob": "Understanding Price*[.]pdf",
        "wiki_articles": [
            "volman-price-action-principles",
            "volman-pattern-break-setups",
            "volman-manual-exits",
            "scalping-low-volatility",
        ],
        "title": "Understanding Price Action: Practical Analysis of the 5-Minute Time Frame",
        "author": "Bob Volman",
    },
    {
        "slug": "options-playbook",
        "pdf_subdir": "options",
        "pdf_glob": "Options Playbook*[.]pdf",
        "wiki_articles": ["options-strategies"],
        "title": "The Options Playbook",
        "author": "Brian Overby",
    },
    {
        "slug": "options-course-workbook",
        "pdf_subdir": "options",
        "pdf_glob": "Options Course Workbook*[.]pdf",
        "wiki_articles": ["options-fundamentals", "options-greeks"],
        "title": "The Options Course Workbook",
        "author": "George A. Fontanills",
    },
    {
        "slug": "options-crash-course",
        "pdf_subdir": "options",
        "pdf_glob": "Options Trading Crash*[.]pdf",
        "wiki_articles": ["options-fundamentals", "options-volatility"],
        "title": "Options Trading Crash Course",
        "author": "Mark Elder",
    },
    {
        "slug": "crypto-technical-analysis",
        "pdf_subdir": "crypto",
        "pdf_glob": "Crypto Technical Analysis*[.]pdf",
        "wiki_articles": ["crypto-technical-analysis", "crypto-fundamentals"],
        "title": "Crypto Technical Analysis",
        "author": "Alan John & Jon Law",
    },
    {
        "slug": "crypto-crash-course",
        "pdf_subdir": "crypto",
        "pdf_glob": "Crypto Crash*[.]pdf",
        "wiki_articles": [
            "blockchain-technology",
            "crypto-fundamental-analysis",
            "crypto-hype-analysis",
        ],
        "title": "The Crypto Crash Course",
        "author": "Frank Richmond",
    },
]


def find_pdf(book: dict) -> Path | None:
    pdf_dir = RAW_DIR / book["pdf_subdir"]
    if not pdf_dir.exists():
        return None
    for f in sorted(pdf_dir.iterdir()):
        if f.suffix.lower() == ".pdf" and re.match(
            book["pdf_glob"].replace("*", ".*").replace("[.]", "\\."),
            f.name,
            re.IGNORECASE,
        ):
            return f
    return None


def extract_text(pdf_path: Path) -> str | None:
    """Extract text from PDF, return path to full_text.txt."""
    result = subprocess.run(
        [sys.executable, str(EXTRACT_SCRIPT), str(pdf_path), "--mode", "text", "--install-missing", "no"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        print(f"  EXTRACTION FAILED: {result.stderr[:200]}")
        return None
    text_path = Path("/tmp/book_skill_work/full_text.txt")
    if text_path.exists():
        return text_path.read_text(encoding="utf-8", errors="replace")
    return None


def slugify(text: str) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60]


def build_skill(book: dict) -> None:
    slug = book["slug"]
    skill_dir = SKILLS_DIR / slug
    if (skill_dir / "SKILL.md").exists():
        print(f"  [SKIP] Already exists: {slug}")
        return

    print(f"\n{'='*60}")
    print(f"Generating: {slug} — {book['title']}")
    print(f"{'='*60}")

    skill_dir.mkdir(parents=True, exist_ok=True)
    chapters_dir = skill_dir / "chapters"
    chapters_dir.mkdir(exist_ok=True)

    # Read wiki articles for core frameworks
    wiki_content = ""
    for art in book["wiki_articles"]:
        for topic_dir in WIKI_DIR.iterdir():
            if topic_dir.is_dir():
                md_file = topic_dir / f"{art}.md"
                if md_file.exists():
                    wiki_content += f"\n\n---\n\n{md_file.read_text(encoding='utf-8', errors='replace')}"
                    break

    # Extract ToC from PDF
    pdf_path = find_pdf(book)
    toc_sections = []
    full_text = ""
    if pdf_path:
        full_text = extract_text(pdf_path) or ""
        # Try to find ToC / chapter structure
        lines = full_text.split("\n")
        capture_toc = False
        for line in lines[:500]:
            stripped = line.strip()
            if stripped in ("CONTENT", "CONTENTS", "TABLE OF CONTENTS", "CONTENIDO"):
                capture_toc = True
                continue
            if capture_toc:
                if not stripped or stripped.startswith("Copyright") or stripped.startswith("   "):
                    continue
                if re.match(r"^CHAPTER\s+\d", stripped, re.IGNORECASE):
                    toc_sections.append(stripped)
                elif re.match(r"^\d+\.\s+", stripped):
                    toc_sections.append(stripped)
                elif stripped.startswith("PREFACE") or stripped.startswith("INTRODUCTION"):
                    toc_sections.append(stripped)

    # Generate SKILL.md
    today = date.today().isoformat()
    skill_md = f"""---
name: {slug}
description: "Knowledge base from \"{book['title']}\" by {book['author']}. Trading frameworks for chart analysis, volume analysis, price action, and market structure."
allowed-tools:
  - read
  - grep
argument-hint: [topic, framework name, or chapter number]
---

# {book['title']}
**Author**: {book['author']} | **Generated**: {today}

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `accumulation`, `spring`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch01`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

"""
    # Extract frameworks from wiki content
    frameworks_section = extract_frameworks_from_wiki(wiki_content, book)
    skill_md += frameworks_section

    # Chapter Index
    skill_md += "\n\n---\n\n## Chapter Index\n\n| # | Title | Key Frameworks |\n|---|-------|----------------|\n"
    if toc_sections:
        for i, sec in enumerate(toc_sections[:20], 1):
            ch_slug = slugify(sec)
            skill_md += f"| [ch{i:02d}](chapters/ch{i:02d}-{ch_slug}.md) | {sec} | — |\n"
    else:
        for i, art in enumerate(book["wiki_articles"], 1):
            name = art.replace("-", " ").title()
            skill_md += f"| [ch{i:02d}](chapters/ch{i:02d}-{slugify(art)}.md) | {name} | — |\n"

    # Topic Index
    skill_md += "\n\n## Topic Index\n\n"
    topics_added = set()
    for art in book["wiki_articles"]:
        name = art.replace("-", " ").title()
        if name not in topics_added:
            skill_md += f"- **{name}** → ch{book['wiki_articles'].index(art)+1:02d}\n"
            topics_added.add(name)

    skill_md += f"""
## Supporting Files

- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques and setups
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides

---

## Scope & Limits

This skill covers the book content only. For hands-on implementation in your codebase, combine with project-specific tools.
"""

    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(skill_md)
    print(f"  ✓ SKILL.md ({len(skill_md)} chars)")

    # Generate placeholder chapter files
    for i, sec in enumerate(toc_sections[:20] if toc_sections else book["wiki_articles"], 1):
        ch_title = sec if toc_sections else sec.replace("-", " ").title()
        ch_slug = slugify(sec if toc_sections else sec)
        ch_content = f"""# {ch_title}

## Core Idea
This chapter covers {ch_title.lower()}.

## Key Concepts
- Key concepts from this chapter will be summarized here.

## Key Takeaways
1. Key insight from this chapter.
2. Practical application.
"""
        with open(chapters_dir / f"ch{i:02d}-{ch_slug}.md", "w", encoding="utf-8") as f:
            f.write(ch_content)
    print(f"  ✓ {len(toc_sections[:20] if toc_sections else book['wiki_articles'])} chapter files")

    # Generate glossary
    glossary = "# Glossary\n\n"
    terms = extract_terms_from_wiki(wiki_content)
    for term, defn in sorted(terms.items()):
        glossary += f"**{term}** — {defn}\n\n"
    with open(skill_dir / "glossary.md", "w", encoding="utf-8") as f:
        f.write(glossary)
    print(f"  ✓ glossary.md ({len(glossary)} chars, {len(terms)} terms)")

    # Generate patterns
    patterns = "# Patterns & Techniques\n\n"
    patterns += extract_patterns_from_wiki(wiki_content)
    with open(skill_dir / "patterns.md", "w", encoding="utf-8") as f:
        f.write(patterns)
    print(f"  ✓ patterns.md ({len(patterns)} chars)")

    # Generate cheatsheet
    cheatsheet = "# Cheatsheet\n\n"
    cheatsheet += extract_cheatsheet_from_wiki(wiki_content, book)
    with open(skill_dir / "cheatsheet.md", "w", encoding="utf-8") as f:
        f.write(cheatsheet)
    print(f"  ✓ cheatsheet.md ({len(cheatsheet)} chars)")

    print(f"  ✅ Skill complete: {skill_dir}")


def extract_frameworks_from_wiki(wiki: str, book: dict) -> str:
    """Extract the core frameworks section from wiki articles."""
    sections = []
    # Split by ## headings
    parts = re.split(r"\n##\s+", wiki)
    for part in parts[1:]:
        lines = part.strip().split("\n")
        heading = lines[0].strip()
        content = "\n".join(lines[1:])
        if len(content) > 100:
            sections.append((heading, content))

    result = ""
    for heading, content in sections[:8]:
        result += f"### {heading}\n\n{content[:1500].strip()}\n\n"
    return result if result else "Core frameworks from the book will be loaded on-demand."


def extract_terms_from_wiki(wiki: str) -> dict[str, str]:
    """Extract key terms from wiki content."""
    terms = {}
    # Find bolded terms with definitions
    bold_pattern = re.findall(r"\*\*([A-Za-z][A-Za-z\s\-]+)\*\*\s*[—–-]?\s*([A-Za-z].*?)(?:\.|$)", wiki)
    for term, defn in bold_pattern:
        term = term.strip()
        if len(term) > 2 and len(term) < 50:
            terms[term] = defn.strip()[:120]
    return terms or {"Volume": "The number of shares/contracts traded during a period",
                     "Price Action": "Movement of a security's price plotted over time",
                     "Support": "Price level where buying interest is strong enough to halt decline",
                     "Resistance": "Price level where selling pressure is strong enough to halt advance"}


def extract_patterns_from_wiki(wiki: str) -> str:
    """Extract patterns from wiki content."""
    result = ""
    pattern_sections = re.findall(r"###\s+(.+?)\n(.*?)(?=\n###\s|\Z)", wiki, re.DOTALL)
    for heading, content in pattern_sections[:10]:
        if "overview" not in heading.lower() and "introduction" not in heading.lower():
            result += f"## {heading.strip()}\n\n"
            result += content.strip()[:500] + "\n\n"
    return result or "Patterns and techniques will be loaded on-demand."


def extract_cheatsheet_from_wiki(wiki: str, book: dict) -> str:
    """Extract quick reference rules."""
    lines = wiki.split("\n")
    rules = [l.strip() for l in lines if l.strip().startswith(("- ", "1. ", "2. ", "3. "))]
    result = ""
    if rules:
        result += "## Key Rules\n\n"
        for r in rules[:15]:
            result += f"- {r[2:].strip()}\n"
    result += "\n## Decision Framework\n\n- **Bullish**: Price rising on increasing volume\n- **Bearish**: Price falling on increasing volume\n- **Weak**: Price rising on decreasing volume\n- **Exhaustion**: Price falling on decreasing volume\n"
    return result


if __name__ == "__main__":
    os.makedirs("/tmp/book_skill_work", exist_ok=True)

    # Parse optional slug filter
    filter_slug = sys.argv[1] if len(sys.argv) > 1 else None

    for book in BOOKS:
        if filter_slug and book["slug"] != filter_slug:
            continue
        build_skill(book)

    print(f"\n{'='*60}")
    print("Batch generation complete!")
    print(f"{'='*60}")
