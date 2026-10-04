# CBAM ontology network and CarbonComply

Ontologies, controlled vocabularies, mappings and a proof-of-concept application for producing EU **Carbon Border Adjustment Mechanism (CBAM)** reports from supplier data using a knowledge graph.

This repository contains:

- **CBAM Common Data Model**: a modular OWL ontology network of 23 ontologies covering the CBAM report structure and the official EU code lists.
- **CarbonComply**: a web application that converts CBAM Communication Templates (Excel) into an RDF knowledge graph and then into a CBAM XML report that is valid against the EU XSD.
- **Validation and evaluation material**: SHACL shapes, competency questions, a performance test and ontology quality reports.

## How it works

```
Communication Templates (.xlsx)
        │  1. parse each worksheet table into CSV
        ▼
CSV tables ──2. enrich with report IDs and controlled-vocabulary IRIs
        │  3. map to RDF with YARRRML (Morph-KGC)
        ▼
RDF knowledge graph  ◄── CBAM ontology network (cbam-network/)
        │  4. validate with SHACL (SHACL/)
        │  5. transform to XML with XSPARQL
        ▼
CBAM XML report ──6. validate against the EU XSD (cbam-specification/)
```

The knowledge graph can also be queried with SPARQL for analysis beyond reporting, e.g. to compare the embedded emissions of installations (see `usecase/competency_questions/`).

## Repository structure

| Folder | Contents |
| --- | --- |
| [`cbam-network/`](cbam-network) | The 23 ontologies of the CBAM Common Data Model (Turtle) and the GeoNames ontology they reuse |
| [`SHACL/`](SHACL) | SHACL shapes generated from the ontologies with Astrea (`astrea-shapes.ttl`), hand-written CBAM business rules (`cbam_business_rules.ttl`), an example knowledge graph (`data.ttl`) and its validation report |
| [`mappings/`](mappings) | YARRRML mappings from template tables to RDF and the XSPARQL mapping from RDF to CBAM XML |
| [`carboncomply/`](carboncomply) | The CarbonComply application: Flask REST backend (`CarbonComply-rest/`) and React frontend (`carboncomply-web/`), with Docker Compose deployment |
| [`cbam-specification/`](cbam-specification) | The EU CBAM Quarterly Report XML schema, version 19.00 |
| [`usecase/`](usecase) | Proof-of-concept inputs (EU example Communication Templates and variants), intermediate CSV files, the generated RDF and XML, and the competency questions with their SPARQL queries and results |
| [`carboncomply_performance_test/`](carboncomply_performance_test) | Performance test with 1 to 50 synthetic templates, including results |
| [`oquare-evaluation/`](oquare-evaluation) | OQuaRE ontology quality metrics, computed automatically on every push by a GitHub Action |
| [`huron-evaluation/`](huron-evaluation) | HURON readability metrics for the ontology network |
| [`Foops_Results/`](Foops_Results) | FOOPS! FAIRness reports (JSON), one per ontology |

## The ontology network

`CBAMReport` is the core ontology. It models the report, its actors (declarant, importer, operator, representative, competent authority), installations, goods, embedded emissions and carbon pricing. It imports the code-list ontologies and the W3C ORG and vCard vocabularies. The other 22 ontologies represent the coded value lists of the EU CBAM templates as controlled vocabularies.

| Ontology | IRI | Content |
| --- | --- | --- |
| CBAM report | `https://purl.org/cbam/cbamreport` | Report structure; imports the code lists |
| CN | `https://purl.org/cbam/CN/` | Combined Nomenclature hierarchy (about 15,000 classes) |
| Goods | `https://purl.org/cbam/cbam_goods/` | CBAM goods and aggregated goods categories |
| Emissions Qualifying Parameters | `https://purl.org/cbam/emissionsqualifyingparameters/` | Qualifying parameters per goods category |
| Production Method | `https://purl.org/cbam/Production_Method/` | Production routes |
| Country, Country Plus | `https://purl.org/cbam/Country/`, `https://purl.org/cbam/CountryPlus/` | Countries, linked to GeoNames |
| Currency, Exchange Rate | `https://purl.org/cbam/Currency/`, `https://purl.org/cbam/Exchange_Rate/` | Currencies and exchange rates |
| Other code lists | `https://purl.org/cbam/<Name>/` | Area of import, coordinate system, customs procedure, electricity determination, emission report, flag, goods document, instrument, parameter value type, product covered, reporting period, reporting rule, role, source of electricity |

Each ontology has a version IRI (`<ontology IRI>1.0`) and Dublin Core metadata. Code lists were generated from the EU templates with Python scripts and completed manually in Protégé.

To use the network, load `cbam-network/CBAMReport.ttl` in Protégé or any OWL tool. If the PURLs do not resolve in your environment, map the imported IRIs to the local files in `cbam-network/`.

## Running CarbonComply

Requirements: Docker and Docker Compose.

```bash
cd carboncomply
docker-compose up
```

Open <http://localhost> in a browser, select one or more Communication Templates (you can use the files in `usecase/`), and click **Convert**. The application shows the generated CBAM XML report and the RDF knowledge graph in Turtle, and both can be downloaded.

Ports and the server name are set in `carboncomply/.env`. The backend also exposes a REST API (`POST /api/uploadFile/`, `POST /api/convert/`). See [`carboncomply/README.md`](carboncomply/README.md) for details.

**Scope of the proof-of-concept.** The input is the EU Communication Template. Report fields that this template does not contain, such as declarant, importer and customs data, are filled with placeholder values. To produce a report for submission, these fields must come from the reporting company's own systems.

## Validation and evaluation

- **SHACL**: validate a knowledge graph against both shape files, for example with the validator included in the performance test:
  ```bash
  java -jar carboncomply_performance_test/shacl-validator-0.0.1.jar -i SHACL/data.ttl -s SHACL/astrea-shapes.ttl
  ```
  The Astrea shapes check structural conformance with the ontologies (node kinds, datatypes, classes). `cbam_business_rules.ttl` adds rules that cannot be derived from OWL: mandatory fields, value ranges, total = direct + indirect emissions, and consistency between CN codes and goods categories.
- **Competency questions**: `usecase/competency_questions/` contains three SPARQL queries (lowest-emission installation per product family, carbon cost per installation, highest indirect emissions) and their results on the example knowledge graph.
- **Performance**: see [`carboncomply_performance_test/README.md`](carboncomply_performance_test/README.md) to reproduce the runtime, memory and validation results.
- **Ontology quality**: OQuaRE results are in `oquare-evaluation/results/`; HURON results are in `huron-evaluation/`.
- **FAIRness**: the 23 ontologies were assessed with [FOOPS!](https://foops.linkeddata.es/). The reports in `Foops_Results/` give an overall score between 0.78 and 0.86 per ontology (mean 0.82), with the result of each individual check.

## Data

All data in this repository are public or synthetic: the example Communication Templates published by the European Commission, variants of them with fictitious installations and simulated values, and synthetic templates generated from these examples for the performance test. No confidential company data are included.

## Citation


The ontology network was first presented in:

> Duque-Ramos, A., et al. (2024). Ontology Network for the Standardization of the EU CBAM Report Data. *OK4I: Ontologies and Knowledge Graphs for Industry*, FOIS 2024, Enschede, Netherlands.


## License

CC0-1.0

## Acknowledgements

This work was carried out by the [Tecnomod group, University of Murcia](https://github.com/tecnomod-um) in collaboration with Siemens Energy, which funded the development of the ontologies.