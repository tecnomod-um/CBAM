import os
from pathlib import Path

from rdflib import Graph

from CommunicationReport import FileNames
from utils.Singleton import Singleton
from models.xml.qreport_19 import Qreport
from xsdata.formats.dataclass.parsers import XmlParser


input_file_path_param = '${inputFile}'
xsparql_jar = Path(Path(__file__).parent, "../resources/tools/xsparql-cli.jar")
rdf_xml_temp_file_name = 'temp.rdf'


class RDF2XMLMappingService(metaclass=Singleton):
    def convert(self, workspace: Path, input_rdf_filename: str, template_mapping_file: Path) -> Qreport:
        xml_output_path = Path(workspace, FileNames.CBAM_COMMUNICATION_XML)
        self._generate_rdf_xml_temp_file(workspace, input_rdf_filename)
        mapping_file = self._generate_mapping_file(workspace, rdf_xml_temp_file_name, template_mapping_file)
        self._execute_mappings(mapping_file, xml_output_path)
        parser = XmlParser()
        report: Qreport = parser.parse(xml_output_path, Qreport)
        self._postprocess(report)
        xml_output_path.unlink()
        return report

    def _generate_rdf_xml_temp_file(self, workspace, input_rdf_filename) -> Path:
        rdf_xml_temp_file_path = Path(workspace, rdf_xml_temp_file_name)
        rdf_input_file_path = Path(workspace, input_rdf_filename)
        graph: Graph = Graph()
        graph.parse(rdf_input_file_path, format='ttl')
        graph.serialize(destination=rdf_xml_temp_file_path, format='xml', encoding='utf-8')
        return rdf_xml_temp_file_path


    def _generate_mapping_file(self, workspace, input_filename: str, template_mapping_filepath: Path) -> Path:
        mapping_file_path = Path(workspace, template_mapping_filepath.name)
        input_file_path = str(Path(workspace, input_filename).absolute())
        with open(template_mapping_filepath, "r+") as template_mapping_file, open(mapping_file_path, "w+") as mapping_file:
            template_contents = template_mapping_file.read()
            mapping_file_content = template_contents.replace(input_file_path_param, input_file_path)
            mapping_file.write(mapping_file_content)
        return mapping_file_path

    def _execute_mappings(self, mapping_filepath: Path, output_xml: Path):
        command = f'java -jar {str(xsparql_jar.absolute())} -f {str(output_xml.absolute())} {str(mapping_filepath.absolute())}'
        os.system(command)

    def _postprocess(self, report: Qreport):
        self._set_sequence_numbers(report)

    def _set_sequence_numbers(self, report: Qreport):
        for imported_good in report.imported_good:
            for goods_emission in imported_good.goods_emissions:
                prod_method_qualifying_params_count = 1
                for prod_method_qualifying_params in goods_emission.prod_method_qualifying_params:
                    prod_method_qualifying_params.sequence_number = prod_method_qualifying_params_count
                    prod_method_qualifying_params_count = prod_method_qualifying_params_count + 1

                    direct_qualifying_parameter_count = 1
                    for direct_qualifying_parameter in prod_method_qualifying_params.direct_qualifying_parameters:
                        direct_qualifying_parameter.sequence_number = direct_qualifying_parameter_count
                        direct_qualifying_parameter_count = direct_qualifying_parameter_count + 1

                    indirect_qualifying_parameter_count = 1
                    for indirect_qualifying_parameter in prod_method_qualifying_params.indirect_qualifying_parameters:
                        indirect_qualifying_parameter.sequence_number = indirect_qualifying_parameter_count
                        indirect_qualifying_parameter_count = indirect_qualifying_parameter_count + 1
