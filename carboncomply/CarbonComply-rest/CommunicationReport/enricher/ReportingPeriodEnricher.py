import copy

from CommunicationReport.parser.ReportingPeriodParser import reporting_period_header
from utils.CommunicationReportUtils import get_report_id

reporting_period_enriched_header = reporting_period_header + ['communication_report_id']


class ReportingPeriodEnricher:
    def __init__(self, communication_report: dict):
        self.communication_report = communication_report

    def enrich(self) -> list:
        report_id = get_report_id(self.communication_report)
        enriched_dict = copy.deepcopy(self.communication_report['ReportingPeriod'])
        for entry in enriched_dict:
            # Report id
            entry['communication_report_id'] = report_id
        return enriched_dict
