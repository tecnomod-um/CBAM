# Mapping files

## Overview

This repository contains the mapping files used for translating the CSV files extracted from Communication Templates into RDF, and for translating this RDF into an XML CBAM.

## Repository Structure



```plaintext
mappings
├── yarrrml/
│   ├── *.yarrrml            # A YARRRML mapping file for each table extracted from the starting excel.
├── xsparql/
│   ├── rdf2xml.xs           # An XSPARQL mapping file for translating RDF into XML
└── README.md                # This README file
```
