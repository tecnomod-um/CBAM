from utils.Singleton import Singleton
import openpyxl


class ExcelService(metaclass=Singleton):

    def extract_csv(self, input_excel, x1, y1, x2, y2, sheet_name=None, separator=";"):
        csv_string = ""
        wb = openpyxl.load_workbook(input_excel)
        if sheet_name is None:
            sheet = wb.worksheets[0]
        else:
            sheet = wb.get_sheet_by_name(sheet_name)

        for i in range(x1, x2):
            csv_line = []
            for j in range(y1, y2):
                cell_value = sheet.cell(row=i, column=j).value
                csv_line.append(cell_value)
            csv_string = csv_string + separator.join(csv_line) + "\n"

        return csv_string.strip()


if __name__ == '__main__':
    service = ExcelService()
    excel_file_path = "/home/fabad/Documentacion_proyectos/siemens/20241Q_POSCO_CBAM Report_02_Gwangyang_BF_Finished.xlsx"
    text = service.extract_csv(excel_file_path, 8, 3, 17, 6, separator="\t")

    print(text)