import time
from pathlib import Path

from lxml.etree import XMLSchema
from pyshacl import validate
from rdflib import Graph
from werkzeug.datastructures import FileStorage
from service.PipelineService import PipelineService
from lxml import etree

test_files_directory = Path('synthetic_cbam_templates')
output_file = Path('/home/fabad/Descargas/cbam_performance_test/performance.tsv')
number_of_iterations = 1
shacl_shapes_path=Path('/home/fabad/CBAM/SHACL/astrea-shapes.ttl')
ontology_folder = Path('/home/fabad/CBAM/cbam-network')
xsd_validation_path = Path('/home/fabad/CBAM/carboncomply/CarbonComply-rest/resources/xml_cbam/v19/QReport_v19.00.xsd')

def load_full_ontology(folder: Path) -> Graph:
    g = Graph()
    for ttl_file in folder.glob("*.ttl"):
        try:
            g.parse(ttl_file, format="turtle")
        except Exception as e:
            print(f"  error parsing {ttl_file.name}: {e}")
    return g

def get_number_of_triples(rdf_graph: Graph) -> int:
    return len(rdf_graph)

def get_rdf_graph(rdf_data: str) -> Graph:
    g = Graph()
    g.parse(data=rdf_data, format='ttl')
    return g

def get_shacl_validation(rdf_graph: Graph, ontology_graph: Graph, shapes_graph: Graph) -> str:
    return ''
    conforms, results_graph, results_text = validate(
        rdf_graph,
        shacl_graph=shapes_graph,
        inference="none",  # optional: "none", "rdfs", "owlrl", "both"
        ont_graph=ontology_graph,
        do_owl_imports=False, # Already loaded
        abort_on_first=False,
        meta_shacl=False,
        advanced=False,
    )
    if conforms:
        return 'Pass'
    else:
        return 'Fail'


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


def load_shapes_graph(shacle_shapes_path):
    shapes_graph = Graph()
    shapes_graph.parse(shacle_shapes_path, format="ttl")
    return shapes_graph


if __name__ == '__main__':
    service = PipelineService()
    #ontology_graph = load_full_ontology(ontology_folder)
    ontology_graph = None
    #shapes_graph = load_shapes_graph(shacl_shapes_path)
    shapes_graph = None
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
        for i in range(number_of_iterations):
            print(f"Calculating {len(file_list)} files; iteration {i}")
            start = time.perf_counter()
            res = service.execute_pipeline(Path(f'/home/fabad/Descargas/cbam_performance_test/{str(len(file_list))}_files'), file_list)
            end = time.perf_counter()
            elapsed_time = end - start
            runtimes.append(elapsed_time)

        data_graph = get_rdf_graph(res.get('rdf'))
        number_of_triples = get_number_of_triples(data_graph)
        shacl_validation = get_shacl_validation(data_graph, ontology_graph, shapes_graph)
        xsd_validation = get_xsd_validation(res.get('xml'), xml_schema)
        average_time = sum(runtimes) / len(runtimes)
        tsv_line = f"{str(len(file_list))}\t{'\t'.join([str(runtime) for runtime in runtimes])}\t{str(average_time)}\t{str(number_of_triples)}\t{shacl_validation}\t{xsd_validation}"
        tsv_result = tsv_result + f"\n{tsv_line}"

    close_files(file_list)
    print(tsv_result)
    with open(output_file, "w+", encoding="utf-8") as f:
        f.write(tsv_result)