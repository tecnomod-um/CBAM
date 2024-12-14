from utils.NormalizeText import normalize, remove_non_numeric_characters

information_details_header = ['name_of_the_installation_english_name_:', 'street_number:', 'economic_activity:',
                              'country:', 'unlocode:', 'coordinates_of_the_main_emission_source_latitude_:',
                              'coordinates_of_the_main_emission_source_longitude_:', 'reporting_period_start:',
                              'reporting_period_end:']

# information_details_def = {
#     "name_of_the_installation_english_name_:": {"row": 12, "col": 7},
#     "street_number:": {"row": 13, "col": 7},
#     "economic_activity:": {"row": 14, "col": 7},
#     "country:": {"row": 15, "col": 7},
#     "unlocode:": {"row": 16, "col": 7},
#     "coordinates_of_the_main_emission_source_latitude_:": {"row": 17, "col": 7},
#     "coordinates_of_the_main_emission_source_longitude_:": {"row": 18, "col": 7},
#     "reporting_period_start:": {"row": 19, "col": 7},
#     "reporting_period_end:": {"row": 20, "col": 7}
# }

information_details_def = {
    "name_of_the_installation_english_name_:": {"row": 12, "col": 7},
    "street_number:": {"row": 13, "col": 7},
    "economic_activity:": {"row": 14, "col": 7},
    "country:": {"row": 16, "col": 7},
    "unlocode:": {"row": 17, "col": 7},
    "coordinates_of_the_main_emission_source_latitude_:": {"row": 18, "col": 7},
    "coordinates_of_the_main_emission_source_longitude_:": {"row": 19, "col": 7},
    "reporting_period_start:": {"row": 20, "col": 7},
    "reporting_period_end:": {"row": 21, "col": 7}
}


class InstallationDetailsParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def parse(self) -> list:
        line = {}
        for var in information_details_header:
            var_col = information_details_def[var]['col']
            var_row = information_details_def[var]['row']
            var_value = self.worksheet.cell(row=var_row, column=var_col).value
            if var in ['coordinates_of_the_main_emission_source_latitude_:', 'coordinates_of_the_main_emission_source_longitude_:']:
                line[var] = remove_non_numeric_characters(var_value)
            else:
                line[var] = var_value

        return [line]


if __name__ == '__main__':
    header = ['Name of the installation (English name):', 'Street, Number:', 'Economic activity:', 'Country:',
              'UNLOCODE:', 'Coordinates of the main emission source (latitude):',
              'Coordinates of the main emission source (longitude):', 'Reporting period start:',
              'Reporting period end:']
    for var in header:
        print(normalize(var))
