import time
import os
import sys
from pathlib import Path
from lxml.etree import XMLSchema
from pyshacl import validate
from rdflib import Graph
from werkzeug.datastructures import FileStorage
import shutil
import subprocess

from lxml import etree

repo_folder = Path(__file__).parent.parent
lib_folder = repo_folder / Path("carboncomply/CarbonComply-rest")
sys.path.append(str(lib_folder.resolve()))

from service.PipelineService import PipelineService

test_folder = repo_folder / Path("carboncomply_performance_test")
output_folder = test_folder / Path("output")
test_files_directory = test_folder / Path('input_synthetic_cbam_templates')
output_file = output_folder / Path('performance.tsv')
number_of_iterations = 5
shacl_shapes_path= repo_folder / Path('SHACL/astrea-shapes.ttl')
ontology_folder = repo_folder / Path('cbam-network')
xsd_validation_path = repo_folder / Path('carboncomply/CarbonComply-rest/resources/xml_cbam/v19/QReport_v19.00.xsd')

jar_path = test_folder / Path("shacl-validator-0.0.1.jar")

os.chdir(lib_folder) # Set the rest service as the working directory

def get_number_of_triples(rdf_graph: Graph) -> int:
    return len(rdf_graph)

def get_rdf_graph(rdf_data: str) -> Graph:
    g = Graph()
    g.parse(data=rdf_data, format='ttl')
    return g

def get_shacl_validation(rdf_data: Path, shapes_data: Path) -> str:
    result = subprocess.run(
        ["java", "-jar", str(jar_path), "-i", str(rdf_data.absolute()), "-s", str(shapes_data.absolute())],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr)
        return "Fail"
    return "Pass"

def get_xsd_validation(xml_content: str, schema: XMLSchema):
    xml_doc = etree.fromstring(xml_content.encode("utf-8"))
    is_valid = schema.validate(xml_doc)
    if is_valid:
        return "Pass"
    else:
        for err in schema.error_log:
            print(err)
        return "Fail"

def add_file(new_file: Path, file_list: list):
    for file in file_list:
        file.seek(0)

    file_list.append(FileStorage(stream=(open(new_file, 'rb')), filename=new_file.name))

def close_files(file_list:list):
    for f in file_list:
        f.close()



if __name__ == '__main__':
    if shutil.which("java") is None:
        raise RuntimeError("Java not found. Required JDK 21 or higher.")
    
    output_folder.mkdir(parents=True, exist_ok=True)
    service = PipelineService()
    xml_schema = etree.XMLSchema(etree.parse(str(xsd_validation_path)))
    file_list = []
    tsv_result = f"Number of files\t{'\t'.join(['Runtime ' + str(x+1) for x in range(number_of_iterations)])}\tAverage\tTriples\tSHACL validation\tXSD validation"
    for file in test_files_directory.iterdir():
        add_file(file, file_list)
        runtimes = []
        number_of_triples = None
        shacl_validation = ''
        xsd_validation = ''
        res = None
        pipeline_output_folder = output_folder / Path(f'{str(len(file_list))}_files')
        for i in range(number_of_iterations):
            print(f"Calculating {len(file_list)} files; iteration {i}")
            start = time.perf_counter()
            res = service.execute_pipeline(pipeline_output_folder, file_list)
            end = time.perf_counter()
            elapsed_time = end - start
            runtimes.append(elapsed_time)

        data_graph = get_rdf_graph(res.get('rdf'))
        number_of_triples = get_number_of_triples(data_graph)
        shacl_validation = get_shacl_validation(pipeline_output_folder / Path('cbam_communication.rdf'), shacl_shapes_path)
        xsd_validation = get_xsd_validation(res.get('xml'), xml_schema)
        average_time = sum(runtimes) / len(runtimes)
        tsv_line = f"{str(len(file_list))}\t{'\t'.join([str(runtime) for runtime in runtimes])}\t{str(average_time)}\t{str(number_of_triples)}\t{shacl_validation}\t{xsd_validation}"
        tsv_result = tsv_result + f"\n{tsv_line}"

    close_files(file_list)
    print(tsv_result)
    with open(output_file, "w+", encoding="utf-8") as f:
        f.write(tsv_result)
