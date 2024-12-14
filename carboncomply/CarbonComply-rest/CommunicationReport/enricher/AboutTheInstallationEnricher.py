import copy

from CommunicationReport.parser.AboutTheInstallationParser import about_the_installation_header
from service.CountryService import CountryService
from utils.CommunicationReportUtils import get_report_id

about_the_installation_enriched_header = about_the_installation_header + ['country_code', 'country_iri', 'communication_report_id']


class AboutTheInstallationEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        country_service = CountryService()
        report_id = get_report_id(self.communication_report)
        enriched_dict = copy.deepcopy(self.communication_report['AboutTheInstallation'])
        for entry in enriched_dict:
            # Country Code
            country_code = self.communication_report['InstallationDetails'][0]['country:']
            entry['country_code'] = country_code

            # Country iri
            country_iri = country_service.get_iri(country_code)
            entry['country_iri'] = country_iri

            # Report id
            entry['communication_report_id'] = report_id
        return enriched_dict
