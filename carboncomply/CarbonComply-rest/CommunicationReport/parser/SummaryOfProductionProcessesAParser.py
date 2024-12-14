from utils.NormalizeText import normalize

summary_of_production_processes_a_header = ['a', 'aggregated_good_produced', 'route_1', 'route_2', 'route_3',
                                            'route_4', 'route_5', 'route_6']

summary_of_production_processes_a_def = {
    "a": {"row": 12, "col": 8},
    "aggregated_good_produced": {"row": 12, "col": 9},
    "route_1": {"row": 12, "col": 10},
    "route_2": {"row": 12, "col": 11},
    "route_3": {"row": 12, "col": 12},
    "route_4": {"row": 12, "col": 13},
    "route_5": {"row": 12, "col": 14},
    "route_6": {"row": 12, "col": 15}
}

class SummaryOfProductionProcessesAParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def _infer_number_of_lines(self):
        a_col = summary_of_production_processes_a_def['a']['col']
        a_row = summary_of_production_processes_a_def['a']['row']
        row_count = 1
        while ('G'+str(row_count)) == self.worksheet.cell(row=a_row, column=a_col).value:
            row_count = row_count + 1
            a_row = a_row + 1

        return row_count - 1

    def _parse_line(self, line_number) -> dict:
        line = {}
        for var in summary_of_production_processes_a_header:
            var_col = summary_of_production_processes_a_def[var]['col']
            var_row = summary_of_production_processes_a_def[var]['row'] + line_number
            line[var] = self.worksheet.cell(row=var_row, column=var_col).value
        return line

    def _empty_line(self, line: dict):
        for var in summary_of_production_processes_a_header:
            if var == 'a':
                continue
            if line[var] is not None:
                return False
        return True

    def parse(self) -> list:
        lines = []
        number_of_lines = self._infer_number_of_lines()
        for line_number in range(number_of_lines):
            line = self._parse_line(line_number)
            if not self._empty_line(line):
                lines.append(line)
        return lines


if __name__ == '__main__':
    header = ['(a)', 'Aggregated good produced', 'Route 1', 'Route 2', 'Route 3', 'Route 4', 'Route 5', 'Route 6']
    for var in header:
        print(normalize(var))
