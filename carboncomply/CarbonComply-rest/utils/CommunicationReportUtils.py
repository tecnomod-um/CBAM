def get_report_id(communication_report: dict) -> str:
    period_start = communication_report['ReportingPeriod'][0]['reporting_period_start'].strftime('%Y%m%d')
    period_end = communication_report['ReportingPeriod'][0]['reporting_period_end'].strftime('%Y%m%d')
    unlocode = communication_report['InstallationDetails'][0]['unlocode:'].replace(' ', '')
    return unlocode + period_start + period_end
