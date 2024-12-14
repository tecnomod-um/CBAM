import csv
from pathlib import Path
import openpyxl

from CommunicationReport import FileNames
from CommunicationReport.parser.AboutTheInstallationParser import AboutTheInstallationParser, about_the_installation_header
from CommunicationReport.parser.InstallationDetailsParser import InstallationDetailsParser, information_details_header
from CommunicationReport.parser.ReportingPeriodParser import reporting_period_header, ReportingPeriodParser
from CommunicationReport.parser.SummaryOfEmissionsParser import summary_of_emissions_header, SummaryOfEmissionsParser
from CommunicationReport.parser.SummaryOfProductionProcessesAParser import summary_of_production_processes_a_header, \
    SummaryOfProductionProcessesAParser
from CommunicationReport.parser.SummaryOfProductionProcessesBParser import summary_of_production_processes_b_header, \
    SummaryOfProductionProcessesBParser
from CommunicationReport.parser.SummaryOfProductsParser import SummaryOfProductsParser, summary_of_products_header

summary_communication_sheet_name = 'Summary_Communication'
instance_data_sheet_name = 'A_InstData'

_communication_report_file_keys = {
    'SummaryOfProducts': {
        'filename': FileNames.CBAM_SUMMARY_OF_PRODUCTS,
        'header': summary_of_products_header
    },
    'InstallationDetails': {
        'filename': FileNames.CBAM_INSTALLATION_DETAILS,
        'header': information_details_header
    },
    'SummaryOfProductionProcessesA': {
        'filename': FileNames.CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_A,
        'header': summary_of_production_processes_a_header
    },
    'SummaryOfProductionProcessesB': {
        'filename': FileNames.CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_B,
        'header': summary_of_production_processes_b_header
    },
    'SummaryOfEmissions': {
        'filename': FileNames.CBAM_SUMMARY_OF_EMISSIONS,
        'header': summary_of_emissions_header
    },
    'AboutTheInstallation': {
        'filename': FileNames.CBAM_ABOUT_THE_INSTALLATION,
        'header': about_the_installation_header
    },
    'ReportingPeriod': {
        'filename': FileNames.CBAM_REPORTING_PERIOD,
        'header': reporting_period_header
    }
}


class CommunicationReportParser:
    def __init__(self, file_path: Path):
        self.workbook = openpyxl.load_workbook(file_path, data_only=True)
        self.summary_of_product_parser = SummaryOfProductsParser(self.workbook[summary_communication_sheet_name])
        self.installation_details_parser = InstallationDetailsParser(self.workbook[summary_communication_sheet_name])
        self.summary_of_production_processes_a_parser = SummaryOfProductionProcessesAParser(
            self.workbook[summary_communication_sheet_name])
        self.summary_of_production_processes_b_parser = SummaryOfProductionProcessesBParser(
            self.workbook[summary_communication_sheet_name])
        self.summary_of_emissions_parser = SummaryOfEmissionsParser(self.workbook[summary_communication_sheet_name])
        self.about_the_installation_parser = AboutTheInstallationParser(self.workbook[instance_data_sheet_name])
        self.reporting_period_parser = ReportingPeriodParser(self.workbook[instance_data_sheet_name])

    def parse(self) -> dict:
        communication_report = {
            'SummaryOfProducts': self.summary_of_product_parser.parse(),
            'InstallationDetails': self.installation_details_parser.parse(),
            'SummaryOfProductionProcessesA': self.summary_of_production_processes_a_parser.parse(),
            'SummaryOfProductionProcessesB': self.summary_of_production_processes_b_parser.parse(),
            'SummaryOfEmissions': self.summary_of_emissions_parser.parse(),
            'AboutTheInstallation': self.about_the_installation_parser.parse(),
            'ReportingPeriod': self.reporting_period_parser.parse()
        }
        return communication_report


if __name__ == '__main__':
    file_path = Path('/home/fabad/Documentacion_proyectos/siemens/CBAM DaZhi 2024.xlsx')
    parser = CommunicationReportParser(file_path)
    report = parser.parse()
    workdir = '/home/fabad/Descargas/CC/francisco.abad@um.es/'
    for key, fileinfo in _communication_report_file_keys.items():
        with open(Path(workdir, fileinfo['filename']), 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fileinfo['header'], delimiter=",")
            writer.writeheader()
            writer.writerows(report[key])

