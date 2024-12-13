from utils.NormalizeText import normalize

summary_of_emissions_header = ['calculation_-_based_excl._pfc_emissions_unit',
                                    'calculation_-_based_excl._pfc_emissions_value', 'total_pfc_emissions_unit',
                                    'total_pfc_emissions_value', 'measurement_-_based_unit',
                                    'measurement_-_based_value', 'other_unit', 'other_value',
                                    'total_direct_emissions_during_reporting_period_unit',
                                    'total_direct_emissions_during_reporting_period_value',
                                    'total_indirect_emissions_during_reporting_period_unit',
                                    'total_indirect_emissions_during_reporting_period_value',
                                    'total_emissions_during_reporting_period_unit',
                                    'total_emissions_during_reporting_period_value',
                                    'general_information_on_data_quality:',
                                    'justification_for_use_of_default_values_if_relevant_:',
                                    'information_on_quality_assurance:']

summary_of_emissions_def = {
    "calculation_-_based_excl._pfc_emissions_unit": {"row": 12, "col": 26},
    "calculation_-_based_excl._pfc_emissions_value": {"row": 13, "col": 26},
    "total_pfc_emissions_unit": {"row": 12, "col": 28},
    "total_pfc_emissions_value": {"row": 13, "col": 28},
    "measurement_-_based_unit": {"row": 12, "col": 30},
    "measurement_-_based_value": {"row": 13, "col": 30},
    "other_unit": {"row": 12, "col": 32},
    "other_value": {"row": 13, "col": 32},
    "total_direct_emissions_during_reporting_period_unit": {"row": 15, "col": 33},
    "total_direct_emissions_during_reporting_period_value": {"row": 15, "col": 34},
    "total_indirect_emissions_during_reporting_period_unit": {"row": 16, "col": 33},
    "total_indirect_emissions_during_reporting_period_value": {"row": 16, "col": 34},
    "total_emissions_during_reporting_period_unit": {"row": 17, "col": 33},
    "total_emissions_during_reporting_period_value": {"row": 17, "col": 34},
    "general_information_on_data_quality:": {"row": 19, "col": 29},
    "justification_for_use_of_default_values_if_relevant_:": {"row": 20, "col": 29},
    "information_on_quality_assurance:": {"row": 21, "col": 29}
}


class SummaryOfEmissionsParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def parse(self) -> list:
        line = {}
        for var in summary_of_emissions_header:
            var_col = summary_of_emissions_def[var]['col']
            var_row = summary_of_emissions_def[var]['row']
            line[var] = self.worksheet.cell(row=var_row, column=var_col).value
        return [line]


if __name__ == '__main__':
    header = ['Calculation - based (excl. PFC emissions)', 'Total PFC emissions', 'Measurement - based', 'Other',
              'Total direct emissions during reporting period:', 'Total indirect emissions during reporting period:',
              'Total emissions during reporting period:', 'General information on data quality:',
              'Justification for use of default values (if relevant):', 'Information on quality assurance:']
    for var in header:
        print(normalize(var))

