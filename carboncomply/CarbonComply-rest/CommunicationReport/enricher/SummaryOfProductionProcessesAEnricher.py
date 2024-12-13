import copy

from CommunicationReport.parser.SummaryOfProductionProcessesAParser import summary_of_production_processes_a_header
from service.TypeOfAggregatedGoodService import TypeOfAggregatedGoodService

summary_of_production_processes_a_enriched_header = summary_of_production_processes_a_header + ['aggregated_good_produced_iri']


class SummaryOfProductionProcessesAEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        aggregated_good_service = TypeOfAggregatedGoodService()
        enriched_dict = copy.deepcopy(self.communication_report['SummaryOfProductionProcessesA'])
        for entry in enriched_dict:
            # Aggregated good IRI
            aggregated_good_label = entry['aggregated_good_produced']
            aggregated_good_label_iri = aggregated_good_service.get_iri(aggregated_good_label)
            entry['aggregated_good_produced_iri'] = aggregated_good_label_iri

        return enriched_dict
