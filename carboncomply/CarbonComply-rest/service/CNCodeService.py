from pathlib import Path

from rdflib import Graph

from utils.Singleton import Singleton
import logging
logger = logging.getLogger(__name__)

cn_ontology_file = Path(Path(__file__).parent, '../resources/ontologies/CNCode.ttl')

class CNCodeService(metaclass=Singleton):

    def __init__(self):
        self._iri_by_cn_code = self._get_iri_by_cn_code_dict()

    def get_iri(self, cn_code: str) -> str:
        return self._iri_by_cn_code.get(cn_code)


    def _get_iri_by_cn_code_dict(self) -> dict:
        iri_by_cn = {}
        ontology = Graph()
        ontology.parse(str(cn_ontology_file.absolute()))
        query = """
                            SELECT ?iri ?code WHERE {
                                ?iri <https://purl.org/cbam/CN/cn_code> ?code .
                            }
                            """
        results = ontology.query(query)
        for row in results:
            iri = row.iri
            code = str(row.code).replace(' ', '')
            iri_by_cn[code] = str(iri)
        return iri_by_cn



if __name__ == '__main__':
    service = CNCodeService()
    print (service.get_iri('73182200'))
