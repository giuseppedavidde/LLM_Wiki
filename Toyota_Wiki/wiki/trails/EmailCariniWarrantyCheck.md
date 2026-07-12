---
title: "Email a Carini — Verifica stato garanzia"
type: trail
tags: [action, email, carini, warranty-check, cws]
sources: [YarisCrossWarrantyStatus, TagliandoPrezziChiari, YarisCrossServiceHistory]
last_updated: 2026-07-12
---

# Email a Carini — Verifica stato garanzia

## Contesto
Dopo l'analisi della [[YarisCrossWarrantyStatus]] è emerso che nell'app MyToyota il **2° tagliando (30.000 km)** risulta non registrato, nonostante sia stato regolarmente eseguito da [[CariniSrl|Carini Tavagnacco]] l'11.10.2024.

## Problema
Possibile discontinuità nel **CWS (Central Warranty System)** Toyota per il cambio di paese Austria → Italia. Questo potrebbe influire su:
- [[ToyotaRelaxPlus]] (IT) vs [[ToyotaRelaxGarantieAT|Toyota Relax Garantie]] (AT) — quale regime si applica?
- [[ToyotaBatteryCare]] — registrazione Battery Health Check

## Azione
Inviata email a Carini con allegato storico fatture (PDF) per chiedere:

1. Perché a Pordenone mi hanno detto che l'auto era "fuori garanzia"?
2. Perché il tagliando 30.000 km non risulta nell'app MyToyota?
3. CWS ha registrato il cambio Austria → Italia? Regime Relax IT o AT?
4. Stato attuale: garanzia ibrida, Relax Plus/AT, Battery Care, Battery Health Check?
5. Batteria 12V — risolta con casa madre?
6. Possibile regolarizzare registrazioni mancanti?

## Destinatario
Carini srl — Assistenza Toyota
- Pordenone (PN): Viale Treviso, 27/A
- Tavagnacco (UD): Via Nazionale, 79

## Allegati
- Storico fatture (dal PDF `raw/service_history/JTDKBABB30A139217_service_history_until_2026.pdf`)

## Follow-up
- [ ] Attendere risposta da Carini
- [ ] Se necessario, contattare Toyota Motor Italia direttamente
- [ ] Aggiornare [[YarisCrossWarrantyStatus]] con esito
