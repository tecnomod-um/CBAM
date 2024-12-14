reporting_period_header = ['reporting_period_start', 'reporting_period_end']

reporting_period_def = {
    'reporting_period_start': {'row': 9, 'col': 9},
    'reporting_period_end': {'row': 9, 'col': 12}
}


class ReportingPeriodParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def parse(self) -> list:
        line = {}
        for var in reporting_period_header:
            var_col = reporting_period_def[var]['col']
            var_row = reporting_period_def[var]['row']
            line[var] = self.worksheet.cell(row=var_row, column=var_col).value
        return [line]

