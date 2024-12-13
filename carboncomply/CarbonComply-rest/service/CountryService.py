from pathlib import Path
from rdflib import Graph
from utils.Singleton import Singleton
import logging
logger = logging.getLogger(__name__)

country_ontology_file = Path(Path(__file__).parent, '../resources/ontologies/CountryPlus.ttl')


class CountryService(metaclass=Singleton):
    def __init__(self):
        self._iri_by_code: dict = self._get_iri_by_code_dict()

    def _get_iri_by_code_dict(self):
        iri_by_code: dict = {}
        ontology = Graph()
        ontology.parse(str(country_ontology_file.absolute()))
        query = """
                    SELECT ?iri ?code WHERE {
                        ?iri <https://www.geonames.org/ontology#countryCode> ?code .
                    }
                    """
        results = ontology.query(query)
        for row in results:
            iri = row.iri
            code = str(row.code)
            iri_by_code[code] = str(iri)
        return iri_by_code

    def get_iri(self, country_code) -> str:
        if country_code in self._iri_by_code.keys():
            return self._iri_by_code[country_code]
        else:
            logger.warning(f'No class found for country code  {country_code}')
            return None
