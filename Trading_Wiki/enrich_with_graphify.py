import json
import re
import os
from pathlib import Path

WIKI_DIR = Path("wiki")
GRAPH_PATH = Path("graphify-out/graph.json")
IMAGES_DIR = Path("graphify-out/images")

with open(GRAPH_PATH) as f:
    graph = json.load(f)

nodes_by_id = {n["id"]: n for n in graph["nodes"]}
nodes_by_label = {}
for n in graph["nodes"]:
    lbl = n.get("label", "")
    if lbl:
        nodes_by_label[lbl.lower()] = n

links_by_source = {}
for l in graph["links"]:
    links_by_source.setdefault(l["source"], []).append(l)

ARTICLE_TO_LABELS = {
    "wyckoff-method-overview": ["Wyckoff Methodology"],
    "wyckoff-2-framework": ["Wyckoff Phases (A-E)", "Wyckoff Method"],
    "volume-price-analysis-vpa": ["Volume Price Analysis (VPA)"],
    "volume-profile": ["Volume Profile"],
    "volume-at-price-vap": ["Volume at Price (VAP)"],
    "springs": ["Spring"],
    "upthrusts": ["Upthrust", "Upthrust After Distribution (UTAD)"],
    "absorption": ["Absorption"],
    "trading-ranges-support-resistance": ["Trading Range", "Support and Resistance"],
    "auction-market-theory": ["Auction Market Theory"],
    "bar-chart-reading": ["Candlestick Chart", "Candlestick Patterns (50)"],
    "contrarian-sentiment-analysis": ["Contrary Opinion Theory", "Sentiment Technicals"],
    "market-ecosystem-participants": ["Smart Money / Insiders", "Market Makers / Specialists"],
    "order-flow-footprint": ["Order Flow", "Footprint Charts"],
    "point-figure-renko": ["Point & Figure Charting", "Renko Chart"],
    "price-action-institutional": ["Price Action"],
    "tape-reading-wis-wave": ["Tape Reading", "Weis Wave"],
    "scalping-low-volatility": ["Price Action"],
    "volman-manual-exits": ["Price Action"],
    "volman-pattern-break-setups": ["Price Action", "Breakout", "Crabel Narrow Range Patterns"],
    "volman-price-action-principles": ["Price Action"],
    "blockchain-technology": ["Blockchain", "Smart Contracts"],
    "crypto-fundamental-analysis": ["Fundamental Analysis"],
    "crypto-fundamentals": ["Cryptocurrency Exchanges", "Cryptocurrency Wallets"],
    "crypto-hype-analysis": ["Hype Analysis"],
    "crypto-technical-analysis": ["Technical Analysis", "Candlestick Chart"],
    "options-fundamentals": ["Call Option", "Put Option"],
    "options-greeks": ["Delta", "Gamma", "Theta", "Vega", "Rho"],
    "options-strategies": ["Vertical Spread", "Iron Condor", "Covered Call",
                          "Long Call", "Long Put", "Short Call", "Short Put",
                          "Long Straddle", "Long Strangle", "Iron Butterfly",
                          "Bull Call Spread", "Bear Put Spread", "Collar",
                          "Cash Secured Put", "Diagonal Spread"],
    "options-volatility": ["Implied Volatility", "Historical Volatility",
                          "Black Scholes Model", "Option Premium", "Vega"],
}

def find_node(label_str):
    key = label_str.lower()
    if key in nodes_by_label:
        return nodes_by_label[key]
    for lbl, node in nodes_by_label.items():
        if key in lbl or lbl in key:
            return node
    return None

def get_connections(node_id):
    connected = set()
    image_links = []
    for l in links_by_source.get(node_id, []):
        target = nodes_by_id.get(l["target"])
        if target and target.get("file_type") != "image":
            connected.add((l["target"], target["label"], l.get("relation", "RELATED_TO")))
        elif target and target.get("file_type") == "image":
            image_links.append((l["target"], target["label"], target.get("source_file", "")))
    for l in graph["links"]:
        if l["target"] == node_id:
            src = nodes_by_id.get(l["source"])
            if src and src.get("file_type") != "image":
                connected.add((l["source"], src["label"], l.get("relation", "RELATED_TO")))
            elif src and src.get("file_type") == "image":
                image_links.append((l["source"], src["label"], src.get("source_file", "")))
    return sorted(connected, key=lambda x: x[1]), image_links

def enrich_article(filepath):
    stem = filepath.stem
    labels = ARTICLE_TO_LABELS.get(stem, [])
    if not labels:
        return False

    with open(filepath) as f:
        content = f.read()
    if "## 🔗 Graph Connections" in content:
        return False

    all_connections = []
    all_images = []
    seen_nodes = set()
    seen_images = set()
    for label in labels:
        node = find_node(label)
        if not node:
            continue
        nid = node["id"]
        if nid in seen_nodes:
            continue
        seen_nodes.add(nid)
        conns, imgs = get_connections(nid)
        all_connections.extend(conns)
        for img_id, img_label, img_file in imgs:
            if img_id not in seen_images:
                all_images.append((img_id, img_label, img_file))
                seen_images.add(img_id)

    if not all_connections and not all_images:
        return False

    all_connections = sorted(set(all_connections), key=lambda x: x[1])

    section = ["", "## 🔗 Graph Connections", ""]
    if all_connections:
        section.append("| Concept | Relation | Source |")
        section.append("|---|---|---|")
        for _, lbl, rel in all_connections[:15]:
            section.append(f"| {lbl} | {rel.replace('_', ' ').title()} | EXTRACTED |")

    if all_images:
        section.append("")
        section.append("### Related Images")
        for _, img_label, img_file in all_images[:6]:
            rel_path = os.path.relpath(img_file, filepath.parent)
            caption = img_label[:60].replace("|", "-")
            section.append(f"![{caption}]({rel_path})")

    section.append("")
    section_str = "\n".join(section)
    content = content.rstrip() + section_str

    with open(filepath, "w") as f:
        f.write(content)
    return True

wiki_files = sorted(WIKI_DIR.glob("**/*.md"))
enriched = 0
skipped = 0
not_mapped = 0
for fp in wiki_files:
    if fp.name in ("index.md", "log.md"):
        continue
    if enrich_article(fp):
        enriched += 1
    else:
        stem = fp.stem
        if stem in ARTICLE_TO_LABELS:
            skipped += 1
        else:
            not_mapped += 1

print(f"Enriched: {enriched}")
print(f"Skipped (already enriched or no connections): {skipped}")
print(f"Not mapped (no article-to-label mapping): {not_mapped}")
print(f"Total wiki articles: {enriched + skipped + not_mapped}")
