
summary_of_products_header = ["nro", "production_process_from_which_the_products_arise",
                              "type_of_aggregated_good_or_precursor", "cn_codes", "cn_name",
                              "product_name_used_for_communication_with_reporting_declarant_eg_on_invoices",
                              "see_direct", "see_indirect", "see_total", "unit", "share_of_emissions_by_default_value",
                              "source_for_electricity_ef", "embedded_electricity_mwh/t",
                              "the_main_reducing_agent_of_the_precursor_if_known", "steel_mill_identification_number",
                              "%_mn", "%_cr", "%_ni", "%_other_alloys", "%_carbon", "t_scrap_per_t_steel",
                              "%_other_materials", "%_pre-consumer_scrap", "t_scrap_per_t_aluminium",
                              "%_non-aluminium_elements", "clinker_factor", "calcined_or_not",
                              "concentration_if_hydrous_solution", "%_nitric_acid", "%_urea", "%_n_contained",
                              "%_n_as_ammonium_nh4+", "%_n_as_nitrate_no3–", "%_n_as_urea",
                              "%_n_in_other_organic_forms", "form_of_carbon_price",
                              "share_of_total_embedded_emissions_covered_by_the_carbon_price",
                              "embedded_emissions_covered_by_the_carbon_price_1",
                              "embedded_emissions_covered_by_the_carbon_price_2", "currency",
                              "carbon_price_cp_due_local_currency_1", "carbon_price_cp_due_local_currency_2",
                              "form_of_rebate", "share_of_embedded_emissions_covered_by_the_rebate",
                              "embedded_emissions_covered_by_rebate_1", "embedded_emissions_covered_by_rebate_2",
                              "amount_of_rebate_local_currency_1", "amount_of_rebate_local_currency_2",
                              "result:_effective_cp_due_1", "result:_effective_cp_due_2"]

summary_of_products_def = {
    "nro": {"row": 26, "col": 3},
    "production_process_from_which_the_products_arise": {"row": 26, "col": 4},
    "type_of_aggregated_good_or_precursor": {"row": 26, "col": 5},
    "cn_codes": {"row": 26, "col": 6},
    "cn_name": {"row": 26, "col": 7},
    "product_name_used_for_communication_with_reporting_declarant_eg_on_invoices": {"row": 26, "col": 8},
    "see_direct": {"row": 26, "col": 9},
    "see_indirect": {"row": 26, "col": 10},
    "see_total": {"row": 26, "col": 11},
    "unit": {"row": 26, "col": 12},
    "share_of_emissions_by_default_value": {"row": 26, "col": 13},
    "source_for_electricity_ef": {"row": 26, "col": 14},
    "embedded_electricity_mwh/t": {"row": 26, "col": 15},
    "the_main_reducing_agent_of_the_precursor_if_known": {"row": 26, "col": 16},
    "steel_mill_identification_number": {"row": 26, "col": 17},
    "%_mn": {"row": 26, "col": 18},
    "%_cr": {"row": 26, "col": 19},
    "%_ni": {"row": 26, "col": 20},
    "%_other_alloys": {"row": 26, "col": 21},
    "%_carbon": {"row": 26, "col": 22},
    "t_scrap_per_t_steel": {"row": 26, "col": 23},
    "%_other_materials": {"row": 26, "col": 24},
    "%_pre-consumer_scrap": {"row": 26, "col": 25},
    "t_scrap_per_t_aluminium": {"row": 26, "col": 26},
    "%_non-aluminium_elements": {"row": 26, "col": 27},
    "clinker_factor": {"row": 26, "col": 28},
    "calcined_or_not": {"row": 26, "col": 29},
    "concentration_if_hydrous_solution": {"row": 26, "col": 30},
    "%_nitric_acid": {"row": 26, "col": 31},
    "%_urea": {"row": 26, "col": 32},
    "%_n_contained": {"row": 26, "col": 33},
    "%_n_as_ammonium_nh4+": {"row": 26, "col": 34},
    "%_n_as_nitrate_no3–": {"row": 26, "col": 35},
    "%_n_as_urea": {"row": 26, "col": 36},
    "%_n_in_other_organic_forms": {"row": 26, "col": 37},
    "form_of_carbon_price": {"row": 26, "col": 38},
    "share_of_total_embedded_emissions_covered_by_the_carbon_price": {"row": 26, "col": 39},
    "embedded_emissions_covered_by_the_carbon_price_1": {"row": 26, "col": 40},
    "embedded_emissions_covered_by_the_carbon_price_2": {"row": 26, "col": 41},
    "currency": {"row": 26, "col": 42},
    "carbon_price_cp_due_local_currency_1": {"row": 26, "col": 43},
    "carbon_price_cp_due_local_currency_2": {"row": 26, "col": 44},
    "form_of_rebate": {"row": 26, "col": 45},
    "share_of_embedded_emissions_covered_by_the_rebate": {"row": 26, "col": 46},
    "embedded_emissions_covered_by_rebate_1": {"row": 26, "col": 47},
    "embedded_emissions_covered_by_rebate_2": {"row": 26, "col": 48},
    "amount_of_rebate_local_currency_1": {"row": 26, "col": 49},
    "amount_of_rebate_local_currency_2": {"row": 26, "col": 50},
    "result:_effective_cp_due_1": {"row": 26, "col": 51},
    "result:_effective_cp_due_2": {"row": 26, "col": 52}
    }


class SummaryOfProductsParser:
    def __init__(self, worksheet):
        self.worksheet = worksheet

    def _infer_number_of_lines(self):
        nro_col = summary_of_products_def['nro']['col']
        nro_row = summary_of_products_def['nro']['row']
        row_count = 1
        while row_count == self.worksheet.cell(row=nro_row, column=nro_col).value:
            row_count = row_count + 1
            nro_row = nro_row + 1

        return row_count - 1

    def _parse_line(self, line_number) -> dict:
        line = {}
        for var in summary_of_products_header:
            var_col = summary_of_products_def[var]['col']
            var_row = summary_of_products_def[var]['row'] + line_number
            line[var] = self.worksheet.cell(row=var_row, column=var_col).value
        return line

    def _empty_line(self, line: dict):
        for var in summary_of_products_header:
            if var == 'nro':
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
