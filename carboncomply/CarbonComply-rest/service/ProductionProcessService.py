from pathlib import Path
from rdflib import Graph
from utils.Singleton import Singleton
import logging

logger = logging.getLogger(__name__)

production_method_iri = 'https://purl.org/cbam/Production_Method/'


class ProductionProcessService(metaclass=Singleton):
    def __init__(self):
        self._iri_by_label = self._get_iri_by_label_dict()

    def _get_iri_by_label_dict(self) -> dict:
        iri_by_label_dict: dict = {}
        ontology = Graph()
        ontology.parse(production_method_iri, format='ttl')
        query = """
                    SELECT ?iri ?label WHERE {
                        ?iri <http://www.w3.org/2000/01/rdf-schema#label> ?label .
                    }
                """
        results = ontology.query(query)
        for row in results:
            iri = row.iri
            label = row.label.lower()
            iri_by_label_dict[label] = str(iri)
        return iri_by_label_dict

    def get_iri(self, label) -> str:
        lower_label = label.lower()
        if lower_label in self._iri_by_label.keys():
            return self._iri_by_label[lower_label]
        else:
            logger.warning(f'No class found for label {label}')
            return None
