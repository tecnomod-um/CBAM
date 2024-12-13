import csv
from pathlib import Path

from CommunicationReport import FileNames
from CommunicationReport.enricher.AboutTheInstallationEnricher import AboutTheInstallationEnricher
from CommunicationReport.enricher.InstallationDetailsEnricher import InstallationDetailsEnricher
from CommunicationReport.enricher.ReportingPeriodEnricher import ReportingPeriodEnricher
from CommunicationReport.enricher.SummaryOfEmissionsEnricher import SummaryOfEmissionsEnricher
from CommunicationReport.enricher.SummaryOfProductionProcessesAEnricher import SummaryOfProductionProcessesAEnricher
from CommunicationReport.enricher.SummaryOfProductionProcessesBEnricher import SummaryOfProductionProcessesBEnricher
from CommunicationReport.enricher.SummaryOfProductsEnricher import SummaryOfProductsEnricher, \
    summary_of_products_enriched_header
from CommunicationReport.parser.CommunicationReportParser import CommunicationReportParser


class CommunicationReportEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> dict:
        communication_report_enriched = {
            'SummaryOfProducts': self._enrich_summary_of_products(),
            'InstallationDetails': self._enrich_installation_details(),
            'SummaryOfEmissions': self._enrich_summary_of_emissions(),
            'SummaryOfProductionProcessesA': self._enrich_summary_of_production_processes_a(),
            'SummaryOfProductionProcessesB': self._enrich_summary_of_production_processes_b(),
            'AboutTheInstallation': self._enrich_about_the_installation(),
            'ReportingPeriod': self._enrich_reporting_period()
        }
        return communication_report_enriched

    def _enrich_summary_of_products(self) -> list:
        enricher = SummaryOfProductsEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_installation_details(self) -> list:
        enricher = InstallationDetailsEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_summary_of_emissions(self) -> list:
        enricher = SummaryOfEmissionsEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_summary_of_production_processes_a(self) -> list:
        enricher = SummaryOfProductionProcessesAEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_summary_of_production_processes_b(self) -> list:
        enricher = SummaryOfProductionProcessesBEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_about_the_installation(self) -> list:
        enricher = AboutTheInstallationEnricher(self.communication_report)
        return enricher.enrich()

    def _enrich_reporting_period(self) -> list:
        enricher = ReportingPeriodEnricher(self.communication_report)
        return enricher.enrich()


if __name__ == '__main__':
    file_path = Path('/home/fabad/Documentacion_proyectos/siemens/CBAM DaZhi 2024.xlsx')
    parser = CommunicationReportParser(file_path)
    report = parser.parse()

    enricher = CommunicationReportEnricher(report)
    enriched_report = enricher.enrich()

    workdir = '/home/fabad/Descargas/CC/francisco.abad@um.es/'
    file = FileNames.CBAM_SUMMARY_OF_PRODUCTS
    with open(Path(workdir, file), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=summary_of_products_enriched_header, delimiter=",")
        writer.writeheader()
        writer.writerows(enriched_report['SummaryOfProducts'])
