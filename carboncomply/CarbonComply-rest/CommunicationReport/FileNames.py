from CommunicationReport.enricher.InstallationDetailsEnricher import information_details_enriched_header
from CommunicationReport.enricher.ReportingPeriodEnricher import reporting_period_enriched_header
from CommunicationReport.enricher.SummaryOfEmissionsEnricher import summary_of_emissions_enriched_header
from CommunicationReport.enricher.SummaryOfProductionProcessesAEnricher import \
    summary_of_production_processes_a_enriched_header
from CommunicationReport.enricher.SummaryOfProductionProcessesBEnricher import \
    summary_of_production_processes_b_enriched_header
from CommunicationReport.enricher.SummaryOfProductsEnricher import summary_of_products_enriched_header
from CommunicationReport.enricher.AboutTheInstallationEnricher import about_the_installation_enriched_header
from mic.enricher.MICEnricher import mic_enriched_header

CBAM_COMMUNICATION_XLSX = 'cbam_communication.xlsx'
CBAM_SUMMARY_OF_PRODUCTS = 'summary_of_products.csv'
CBAM_INSTALLATION_DETAILS = 'installation_details.csv'
CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_A = 'summary_of_production_processes_a.csv'
CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_B = 'summary_of_production_processes_b.csv'
CBAM_SUMMARY_OF_EMISSIONS = 'summary_of_emissions.csv'
CBAM_ABOUT_THE_INSTALLATION = 'about_the_installation.csv'
CBAM_REPORTING_PERIOD = 'reporting_period.csv'

CBAM_COMMUNICATION_RDF = 'cbam_communication.rdf'
CBAM_COMMUNICATION_XML = 'cbam_communication.xml'

MIC_XLSX = 'mic.xlsx'
MIC = 'mic.csv'
MIC_RDF = 'mic.rdf'

MORPHKG_CONFIG_FILE = 'config.ini'


COMMUNICATION_REPORT_EXPORT_CSV_CONFIG = {
    'SummaryOfProducts': {
        'filename': CBAM_SUMMARY_OF_PRODUCTS,
        'header': summary_of_products_enriched_header
    },
    'InstallationDetails': {
        'filename': CBAM_INSTALLATION_DETAILS,
        'header': information_details_enriched_header
    },
    'SummaryOfProductionProcessesA': {
        'filename': CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_A,
        'header': summary_of_production_processes_a_enriched_header
    },
    'SummaryOfProductionProcessesB': {
        'filename': CBAM_SUMMARY_OF_PRODUCTION_PROCESSES_B,
        'header': summary_of_production_processes_b_enriched_header
    },
    'SummaryOfEmissions': {
        'filename': CBAM_SUMMARY_OF_EMISSIONS,
        'header': summary_of_emissions_enriched_header
    },
    'AboutTheInstallation': {
        'filename': CBAM_ABOUT_THE_INSTALLATION,
        'header': about_the_installation_enriched_header
    },
    'ReportingPeriod': {
        'filename': CBAM_REPORTING_PERIOD,
        'header': reporting_period_enriched_header
    }
}

MIC_EXPORT_CSV_CONFIG = {
    'filename': MIC,
    'header': mic_enriched_header
}