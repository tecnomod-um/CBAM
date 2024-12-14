from utils.NormalizeText import normalize

summary_of_production_processes_b_header = ['b', 'production_process', 'aggregated_goods_category',
                                            '1', '2', '3', '4', '5', '6']

summary_of_production_processes_b_def = {
    "b": {"row": 12, "col": 16},
    "production_process": {"row": 12, "col": 17},
    "aggregated_goods_category": {"row": 12, "col": 18},
    "1": {"row": 12, "col": 19},
    "2": {"row": 12, "col": 20},
    "3": {"row": 12, "col": 21},
    "4": {"row": 12, "col": 22},
    "5": {"row": 12, "col": 23},
    "6": {"row": 12, "col": 24}
}


class SummaryOfProductionProcessesBParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def _infer_number_of_lines(self):
        b_col = summary_of_production_processes_b_def['b']['col']
        b_row = summary_of_production_processes_b_def['b']['row']
        row_count = 1
        while ('P'+str(row_count)) == self.worksheet.cell(row=b_row, column=b_col).value:
            row_count = row_count + 1
            b_row = b_row + 1

        return row_count - 1

    def _parse_line(self, line_number) -> dict:
        line = {}
        for var in summary_of_production_processes_b_header:
            var_col = summary_of_production_processes_b_def[var]['col']
            var_row = summary_of_production_processes_b_def[var]['row'] + line_number
            line[var] = self.worksheet.cell(row=var_row, column=var_col).value
        return line

    def _empty_line(self, line: dict):
        for var in summary_of_production_processes_b_header:
            if var == 'b':
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
    header = ['(b)', 'Production process', 'Aggregated goods category', '1', '2', '3', '4', '5', '6']
    for var in header:
        print(normalize(var))
