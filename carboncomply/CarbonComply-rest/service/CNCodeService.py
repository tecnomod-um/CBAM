from pathlib import Path

from utils.Singleton import Singleton
from owlready2 import *
import logging
logger = logging.getLogger(__name__)

cn_ontology_file = Path(Path(__file__).parent, '../resources/ontologies/CNCodeMod.owl')

class CNCodeService(metaclass=Singleton):

    def __init__(self):
        self._iri_by_cn_code = self._get_iri_by_cn_code_dict()

    def get_iri(self, cn_code: str) -> str:
        return self._iri_by_cn_code.get(cn_code)

    def _get_iri_by_cn_code_dict(self) -> dict:
        cn_ontology = get_ontology(f"file://{str(cn_ontology_file.absolute())}").load()
        iri_by_cn = {}
        for cls in cn_ontology.classes():
            if not self._contains_cn_code(cls):
                continue
            cn_codes = cls.cn_code
            cls_iri = cls.iri
            if len(cn_codes) > 1:
                logger.warning(f'Several CN codes for the iri {cls_iri}')
            elif len(cn_codes) == 0:
                logger.warning(f'No CN codes for the iri {cls_iri}')
            else:
                cn_code = cn_codes[0].replace(' ', '')
                if cn_code.isnumeric():
                    iri_by_cn[cn_code] = cls_iri
                else:
                    logger.warning(f'CN code is not numeric for the iri {cls_iri}')
        cn_ontology.destroy(update_relation=True, update_is_a=True)
        return iri_by_cn

    def _contains_cn_code(self, cls) -> bool:
        try:
            cls.cn_code
        except AttributeError as e:
            return False
        return True


if __name__ == '__main__':
    service = CNCodeService()
    print (service.get_iri('73182200'))
