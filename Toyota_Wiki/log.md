# Toyota_Wiki — Log

## [2026-07-12] Init | Structure created
- Created wiki structure at `~/Progetti/Github/LLM_Wiki/Toyota_Wiki/`
- raw/italy_warranty: added `Termini_Battery_Care_Italia.pdf` (1.7 MB)
- raw/italy_warranty: added `Yaris_Cross_Brochure.pdf` (4.2 MB) — official brochure
- raw/italy_warranty: added `Yaris_Cross_Listino.pdf` (443 KB) — price & specs
- raw/austria_warranty: added `Toyota_Relax_Garantiebedingungen_August_2022.pdf` (118 KB)
- Pending: ingest of all sources

## [2026-07-12] Audit | PDF availability check
- **Italia**: 1 PDF garanzia (Battery Care) + 2 PDF commerciali (brochure, listino). Condizioni Relax Plus e garanzia generale SOLO su pagine web (no PDF).
- **Austria**: 1 PDF garanzia (Relax Garantiebedingungen). Neuwagen-Garantie e Hybrid-Garantie SOLO su pagine web (no PDF).

## [2026-07-12] Web sources saved | raw/italy_warranty + raw/austria_warranty
- Saved 5 web page sources for Italy as .md files
- Saved 2 web page sources for Austria as .md files

## [2026-07-12] New source | raw/service_history
- Added service history PDF for Yaris Cross (VIN: JTDKBABB30A139217)

## [2026-07-12] INGEST | All sources processed
- **PDFs ingested**: Termini_Battery_Care_Italia.pdf → [[TerminiBatteryCareItalia]]
- **PDFs ingested**: Toyota_Relax_Garantiebedingungen_AT.pdf → [[ToyotaRelaxGarantiebedingungenAT]]
- **PDFs ingested (OCR)**: Service history → [[YarisCrossServiceHistory]]
- **Entities created**: [[ToyotaMotorItalia]], [[ToyotaAustriaGmbH]], [[CariniSrl]]
- **Concepts created**: [[ToyotaRelaxPlus]], [[ToyotaRelaxGarantieAT]], [[ToyotaBatteryCare]]
- **Synthesis created**: [[YarisCrossWarrantyStatus]]
- **Updated**: overview.md, index.md
- **Pending**: graph build

## [2026-07-12] FIX | Collegato CariniSrl alla synthesis
- Aggiunti 5 wikilink [[CariniSrl]] in [[YarisCrossWarrantyStatus]]
- CariniSrl ora è referenziata dagli overlay di synthesis (rimane hub isolato nel grafo principale per architettura — è un dealer entity, non un hub di garanzia)

## [2026-07-12] LINT | Health check pass
- **Link rotti**: 5 trovati e riparati:
  - ❌ [[Appendice1CoperturaRelax]] → rimosso wikilink
  - ❌ [[EurocareAssistance]] → sostituito con testo
  - ❌ [[HybridGarantieAT]] + [[NeuwagenGarantieAT]] → sostituiti con wikilink a concept esistenti
  - ❌ [[ToyotaWarrantyFramework]] → reindirizzato a [[overview]]
- **Orfani**: ✅ nessuno (index.md linka tutto)
- **Frontmatter**: ✅ tutte le 12 pagine complete
- **Stale**: ✅ nessuna pagina obsoleta
- **Risultato**: ✅ Wiki in buona salute

## [2026-07-12] New source | Tagliando Prezzi Chiari Yaris Cross
- Added `raw/italy_warranty/Tagliando_Prezzi_Chiari_Yaris_Cross.md`
- **Prezzi ufficiali 2026 ottenuti LIVE dal sito Toyota** via Playwright headless browsing
- Flusso: calcolatore-tagliando.toyota.it → Hybrid → Yaris Cross (id=39) → 1.5 Hybrid (id=20)
- Include: tabella prezzi (€ 323,37 ÷ 678,18), operazioni per intervallo (dettaglio anno per anno), confronto fatture reali con checklist ✅/❌

## [2026-07-12] INGEST | TagliandoPrezziChiari
- Created source page [[TagliandoPrezziChiari]] in wiki/sources/
- Updated overview.md with maintenance schedule section
- Rebuilt graph: **10 nodi, 14 edges** (+1 nodo, +4 edges)
- New source assigned to cluster `toyota-italy`

## [2026-07-12] LINT+FIX + GRAPH rebuild
- **Riparato** frontmatter mancante su index.md (aggiunto title, type, last_updated)
- **Riparati** 4 orfani aggiungendo wikilink:
  - `[[overview]]` in index.md
  - `[[ToyotaAustriaGmbH]]` in ToyotaRelaxGarantieAT.md
  - `[[ToyotaMotorItalia]]` in ToyotaRelaxPlus.md
  - `[[TerminiBatteryCareItalia]]` in ToyotaBatteryCare.md
- **Rebuild grafo**: 10 nodi, **17 edges** (da 14)
- **Lint finale**: 0 rotti, 0 orfani, frontmatter completo ✅

## [2026-07-12] TRAIL | EmailCariniWarrantyCheck
- Creata pagina trail `wiki/trails/EmailCariniWarrantyCheck.md`
- Bozza email per Carini con richiesta verifica:
  - Tagliando 30.000 km non presente in app MyToyota
  - Conferma regime Relax (IT vs AT)
  - Verifica Battery Health Check registrato

## [2026-07-12] GRAPH | Knowledge graph built
- **Graph**: 9 nodi, 10 edges (tutti EXTRACTED da wikilink references)
- **Nodi**: 3 concept, 3 entity, 3 source
- **Top hub**: ToyotaBatteryCare (3 inbound), ToyotaRelaxPlus (3)
- **Clusters** (Leiden, RB-Configuration):
  - #0 `toyota-italy`: ToyotaBatteryCare + ToyotaRelaxPlus + ToyotaMotorItalia
  - #1 `toyota-austria`: ToyotaRelaxGarantieAT + ToyotaAustriaGmbH
  - Isolated: CariniSrl (dealer che connette IT e AT)
- **Unassigned sources**: 3 (le pagine source raw)
- **Contraddizioni**: 0
- **Dipendenze**: 11 pagine indicizzate
- **Output**: graph/_graph.json, _clusters.json, _pages.json, _dependencies.json, _overlays.json
