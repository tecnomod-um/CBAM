from rdflib import Graph

from utils.Singleton import Singleton
import logging
logger = logging.getLogger(__name__)

cn_ontology_iri = 'https://purl.org/cbam/CN'

class CNCodeService(metaclass=Singleton):

    def __init__(self):
        self._iri_by_cn_code = self._get_iri_by_cn_code_dict()

    def get_iri(self, cn_code: str) -> str:
        return self._iri_by_cn_code.get(cn_code)

    def _get_iri_by_cn_code_dict(self) -> dict:
        cn_graph = Graph()
        cn_graph.parse(cn_ontology_iri, format='ttl')
        iri_by_code = {}
        query = """
            PREFIX cn: <https://purl.org/cbam/CN/>
            SELECT ?iri ?code WHERE {
                ?iri cn:cn_code ?code .
            }
        """
        results = cn_graph.query(query)
        for row in results:
            iri = row.iri
            code = str(row.code).replace(' ', '')
            iri_by_code[code] = str(iri)
        return iri_by_code


if __name__ == '__main__':
    service = CNCodeService()
    print (service.get_iri('73182200'))
