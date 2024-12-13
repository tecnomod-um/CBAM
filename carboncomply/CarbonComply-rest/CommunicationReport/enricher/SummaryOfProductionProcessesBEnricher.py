import copy

from CommunicationReport.parser.SummaryOfProductionProcessesBParser import summary_of_production_processes_b_header
from service.TypeOfAggregatedGoodService import TypeOfAggregatedGoodService

summary_of_production_processes_b_enriched_header = (summary_of_production_processes_b_header +
                                                     ['aggregated_goods_category_iri'])


class SummaryOfProductionProcessesBEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        aggregated_good_service = TypeOfAggregatedGoodService()
        enriched_dict = copy.deepcopy(self.communication_report['SummaryOfProductionProcessesB'])
        for entry in enriched_dict:
            # Aggregated good IRI
            aggregated_good_label = entry['aggregated_goods_category']
            aggregated_good_label_iri = aggregated_good_service.get_iri(aggregated_good_label)
            entry['aggregated_goods_category_iri'] = aggregated_good_label_iri
        return enriched_dict
