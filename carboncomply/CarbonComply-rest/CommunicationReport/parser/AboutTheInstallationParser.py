from utils.NormalizeText import normalize, remove_non_numeric_characters

about_the_installation_header = ['name_of_the_installation', 'name_of_the_installation_english_name', 'street_number', 'economic_activity', 'post_code', 'po_box', 'city', 'country', 'unlocode', 'coordinates_of_the_main_emission_source_latitude', 'coordinates_of_the_main_emission_source_longitude', 'name_of_authorized_representative', 'email', 'telephone']

about_the_installation_def = {
    'name_of_the_installation': {'row': 19, 'col': 9},
    'name_of_the_installation_english_name': {'row': 20, 'col': 9},
    'street_number': {'row': 21, 'col': 9},
    'economic_activity': {'row': 22, 'col': 9},
    'post_code': {'row': 23, 'col': 9},
    'po_box': {'row': 24, 'col': 9},
    'city': {'row': 25, 'col': 9},
    'country': {'row': 26, 'col': 9},
    'unlocode': {'row': 27, 'col': 9},
    'coordinates_of_the_main_emission_source_latitude': {'row': 28, 'col': 9},
    'coordinates_of_the_main_emission_source_longitude': {'row': 29, 'col': 9},
    'name_of_authorized_representative': {'row': 30, 'col': 9},
    'email': {'row': 31, 'col': 9},
    'telephone': {'row': 32, 'col': 9}
}


class AboutTheInstallationParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def parse(self) -> list:
        line = {}
        for var in about_the_installation_header:
            var_col = about_the_installation_def[var]['col']
            var_row = about_the_installation_def[var]['row']
            var_value = self.worksheet.cell(row=var_row, column=var_col).value
            if var in ['coordinates_of_the_main_emission_source_latitude', 'coordinates_of_the_main_emission_source_longitude']:
                line[var] = remove_non_numeric_characters(var_value)
            else:
                line[var] = var_value
        return [line]


if __name__ == '__main__':
    header = ['Name of the installation (optional):', 'Name of the installation (English name):', 'Street, Number:', 'Economic activity:', 'Post code:', 'P.O. Box:', 'City:', 'Country:', 'UNLOCODE:', 'Coordinates of the main emission source (latitude):', 'Coordinates of the main emission source (longitude):', 'Name of authorized representative:', 'Email:', 'Telephone:']
    for var in header:
        print(normalize(var))
