# FAIR evaluation of the CBAM Common Data Model with FOOPS!

This folder contains the FOOPS! assessment of the 23 ontologies in `cbam-network/`, reported in Table 5 of the manuscript.

## Set-up

- **Tool:** FOOPS! v0.4.0 ([oeg-upm/fair_ontologies](https://github.com/oeg-upm/fair_ontologies/releases/tag/v0.4.0)), run locally.
- **Date:** 2026-10-04.
- **Input:** the 23 Turtle files in `cbam-network/`. Their SHA-256 checksums are listed in `input_checksums.sha256`.
- **Mode:** file assessment (`POST /assessOntologyFile`). In this mode FOOPS! runs 15 checks: Findable (PURL1, OM1, FIND1, VER1), Interoperable (RDF1, VOC1, VOC2) and Reusable (OM2, OM3, OM4_1, OM4_2, OM5_1, OM5_2, VOC3, VOC4). Accessible checks run only in URI mode and were not assessed.

## Files

| File | Content |
|---|---|
| `reports/*.json` | Original FOOPS! report for each ontology |
| `foops_summary_2026-10-04_final.csv` | Pass/fail of each check per ontology |
| `foops_scores_by_principle_2026-10-04.csv` | Score per FAIR principle and overall score per ontology, with the mean |
| `foops_scores_by_principle_2026-10-04.json` | Same values with the description of the computation |

## Scoring

Each check scores `total_passed_tests / total_tests_run`. The score of a principle is the mean of its checks, and the overall score is the mean of the 15 checks; it equals the `overall_score` returned by FOOPS!.

Check OM4_2 (license resolvable) failed for all ontologies because the execution environment had no access to creativecommons.org; it is counted as failed in all scores.

## Reproduction

```bash
curl -L -o foops.jar https://github.com/oeg-upm/fair_ontologies/releases/download/v0.4.0/fair_ontologies-0.4.0.jar
java -jar foops.jar --server.port=8083 \
     --spring.servlet.multipart.max-file-size=200MB --spring.servlet.multipart.max-request-size=200MB

# in another terminal, for each ontology:
curl -X POST http://localhost:8083/assessOntologyFile \
     -H "accept: application/json" -F "file=@cbam-network/Flag.ttl" > Flag.json
```

The size options are needed for `CNCode.ttl` (12 MB).
