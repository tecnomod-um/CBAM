import copy

from CommunicationReport.parser.InstallationDetailsParser import information_details_header
from service.CountryService import CountryService
from utils.CommunicationReportUtils import get_report_id

information_details_enriched_header = information_details_header + ['country:_iri', 'communication_report_id']


class InstallationDetailsEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        country_service = CountryService()
        enriched_dict = copy.deepcopy(self.communication_report['InstallationDetails'])
        for entry in enriched_dict:
            # Country iri
            country_code = entry['country:']
            country_iri = country_service.get_iri(country_code)
            entry['country:_iri'] = country_iri

            # Report id
            report_id = get_report_id(self.communication_report)
            entry['communication_report_id'] = report_id
        return enriched_dict
