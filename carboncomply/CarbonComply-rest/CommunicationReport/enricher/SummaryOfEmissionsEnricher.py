import copy

from CommunicationReport.parser.SummaryOfEmissionsParser import summary_of_emissions_header
from utils.CommunicationReportUtils import get_report_id

summary_of_emissions_enriched_header = summary_of_emissions_header + ['installation_unlocode', 'communication_report_id']


class SummaryOfEmissionsEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        enriched_dict = copy.deepcopy(self.communication_report['SummaryOfEmissions'])
        report_id = get_report_id(self.communication_report)
        installation_unlocode = self.communication_report['InstallationDetails'][0].get('unlocode:')
        for entry in enriched_dict:
            # Installation unlocode
            entry['installation_unlocode'] = installation_unlocode

            # Communication report id
            entry['communication_report_id'] = report_id
        return enriched_dict
