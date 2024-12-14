import copy

from CommunicationReport.parser.SummaryOfProductsParser import summary_of_products_header
from service.CNCodeService import CNCodeService
from service.ProductionProcessService import ProductionProcessService
from service.TypeOfAggregatedGoodService import TypeOfAggregatedGoodService
from utils.CommunicationReportUtils import get_report_id

summary_of_products_enriched_header = (summary_of_products_header +
                                       ['installation_unlocode', 'cn_iri', 'type_of_aggregated_good_or_precursor_iri',
                                        'production_process_from_which_the_products_arise_iri', 'communication_report_id'])


class SummaryOfProductsEnricher:

    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        cn_service = CNCodeService()
        aggregated_good_service = TypeOfAggregatedGoodService()
        production_process_service = ProductionProcessService()
        enriched_dict = copy.deepcopy(self.communication_report['SummaryOfProducts'])
        installation_unlocode = self.communication_report['InstallationDetails'][0].get('unlocode:')
        report_id = get_report_id(self.communication_report)
        for entry in enriched_dict:
            # Installation unlocode
            entry['installation_unlocode'] = installation_unlocode

            # CN Code IRI
            cn_code = entry['cn_codes']
            cn_iri = cn_service.get_iri(cn_code)
            entry['cn_iri'] = cn_iri

            # Aggregated good IRI
            aggregated_good_label = entry['type_of_aggregated_good_or_precursor']
            aggregated_good_label_iri = aggregated_good_service.get_iri(aggregated_good_label)
            entry['type_of_aggregated_good_or_precursor_iri'] = aggregated_good_label_iri

            # Production process IRI
            production_process_label = entry['production_process_from_which_the_products_arise']
            production_process_iri = production_process_service.get_iri(production_process_label)
            entry['production_process_from_which_the_products_arise_iri'] = production_process_iri

            # Report id
            entry['communication_report_id'] = report_id
        return enriched_dict
