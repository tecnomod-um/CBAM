from pathlib import Path

from rdflib import Graph

from CommunicationReport import FileNames
from utils.Singleton import Singleton

import morph_kgc


summary_of_products_csv_path_param = '${summary_of_products_path}'
installation_details_csv_path_param = '${installation_details_path}'
summary_of_emissions_csv_path_param = '${summary_of_emissions_path}'
about_the_installation_csv_path_param = '${about_installation_path}'
reporting_period_csv_path_param = '${reporting_period_path}'
mic_csv_path_param = '${mic_path}'

input_path_params = [summary_of_products_csv_path_param, installation_details_csv_path_param,
                     summary_of_emissions_csv_path_param, about_the_installation_csv_path_param,
                     reporting_period_csv_path_param, mic_csv_path_param]


class CSV2RDFMappingService(metaclass=Singleton):
    def convert(self, workspace: Path, input_csv_filename: str, template_mapping_files: list) -> Graph:
        mapping_files = self._generate_mapping_files(workspace, input_csv_filename, template_mapping_files)
        global_graph: Graph = Graph()
        for mapping_file in mapping_files:
            morph_kgc_config = self._generate_morph_config(workspace, mapping_file.name)
            graph = morph_kgc.materialize(morph_kgc_config)
            local_graph_filepath = Path(workspace, mapping_file.name + '.rdf')
            graph.serialize(destination=local_graph_filepath, format='turtle', encoding='utf-8')
            global_graph.parse(local_graph_filepath, format='turtle', encoding='utf-8')
            local_graph_filepath.unlink()
        return global_graph



    def _generate_mapping_files(self, workspace: Path, input_filename: str, template_mapping_files: list):
        mapping_files_paths = []
        for template_mapping_file in template_mapping_files:
            mapping_file_path = self._generate_mapping_file(workspace, input_filename, template_mapping_file)
            mapping_files_paths.append(mapping_file_path)

        return mapping_files_paths

    def _generate_mapping_file(self, workspace, input_filename: str, template_mapping_filepath: Path):
        mapping_file_path = Path(workspace, template_mapping_filepath.name)
        input_file_path = str(Path(workspace, input_filename).absolute())
        with (open(template_mapping_filepath, "r+") as template_mapping_file, open(mapping_file_path, "w+") as mapping_file):
            template_contents = template_mapping_file.read()
            #TODO: This requires to have only one input file per yarrrml mapping!
            mapping_file_content = template_contents
            for param in input_path_params:
                mapping_file_content = mapping_file_content.replace(param, input_file_path)
            mapping_file.write(mapping_file_content)
        return mapping_file_path

    def _generate_morph_config(self, workspace, mapping_filename: str) -> str:
        mapping_filepath = Path(workspace, mapping_filename)
        udfs_file_path = Path(Path(__file__).parent, '../utils/MappingFunctions.py')
        morph_config_content_lines = ['[CONFIGURATION]',
                                      f'udfs={udfs_file_path}',
                                      '[DataSource_CSV]',
                                      f'mappings={str(mapping_filepath)}']
        return "\n".join(morph_config_content_lines)


if __name__ == '__main__':
    mapping_file_templates = []
    mapping_file_templates.append(Path('../resources/mapping_definition/summary_of_products.yaml'))
    service = CSV2RDFMappingService()

    workdir = Path('/home/fabad/Descargas/CC/francisco.abad@um.es/')
    input_file_name = FileNames.CBAM_SUMMARY_OF_PRODUCTS
    output_file_name = FileNames.CBAM_COMMUNICATION_RDF
    graph = service.convert(workdir, input_file_name, mapping_file_templates)

    output_file_path = Path(workdir, output_file_name)
    graph.serialize(destination=output_file_path, format='turtle', encoding='utf-8')
