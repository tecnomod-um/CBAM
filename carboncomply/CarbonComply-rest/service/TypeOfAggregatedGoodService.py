from pathlib import Path

from rdflib import Graph

from utils.Singleton import Singleton
import logging
logger = logging.getLogger(__name__)

type_of_aggregated_good_ontology_file = Path(Path(__file__).parent, '../resources/ontologies/cbam_goods_mappingLabel.rdf')


class TypeOfAggregatedGoodService(metaclass=Singleton):
    def __init__(self):
        self._iri_by_label: dict = self._get_iri_by_label_dict()

    def _get_iri_by_label_dict(self) -> dict:
        iri_by_label_dict: dict = {}
        ontology = Graph()
        ontology.parse(str(type_of_aggregated_good_ontology_file.absolute()))
        query = """
            SELECT ?iri ?normalized_label WHERE {
                ?iri <http://www.w3.org/2000/01/rdf-schema#label> ?normalized_label .
            }
            """
        results = ontology.query(query)
        for row in results:
            iri = row.iri
            normalized_label = row.normalized_label
            label = normalized_label.replace('_', ' ').lower()
            iri_by_label_dict[label] = str(iri)
        return iri_by_label_dict

    def get_iri(self, label) -> str:
        lower_label = label.lower()
        if lower_label in self._iri_by_label.keys():
            return self._iri_by_label[lower_label]
        else:
            logger.warning(f'No class found for label {label}')
            return None


if __name__ == '__main__':
    service = TypeOfAggregatedGoodService()
    print (service.get_iri('Iron or steel products'))
