from pathlib import Path

from rdflib import Graph

ontologies = {}

@udf(
    fun_id='http://functions.com/get_property_value',
    ontology_path='http://functions.com/parameters#ontologyParam',
    entity_iri='http://functions.com/parameters#entityParam',
    property_iri='http://functions.com/parameters#propertyParam'
)
def get_property_value(ontology_path: str, entity_iri: str, property_iri: str) -> str:
    global ontologies
    if ontology_path not in ontologies.keys():
        g = Graph()
        g.parse(ontology_path)
        ontologies[ontology_path] = g

    ontology = ontologies.get(ontology_path)

    results = list(ontology.query(f"""
           SELECT ?value
           {{ <{entity_iri}> <{property_iri}> ?value }}
    """))

    if len(results) == 0:
        return ''
    return results.pop()[0]


@udf(
    fun_id='http://functions.com/belongs_to_class',
    ontology_path='http://functions.com/parameters#ontologyParam',
    instance_iri='http://functions.com/parameters#instanceParam',
    class_iri='http://functions.com/parameters#classParam'
)
def belong_to_class(ontology_path: str, instance_iri: str, class_iri: str) -> bool:
    global ontologies
    if ontology_path not in ontologies.keys():
        g = Graph()
        g.parse(ontology_path)
        ontologies[ontology_path] = g

    ontology = ontologies.get(ontology_path)

    results = list(ontology.query(f"""
               ASK
               {{ <{instance_iri}> rdf:type/rdfs:subclassOf* <{class_iri}> }}
        """))
    return bool(results[0])


@udf(
    fun_id='http://functions.com/get_belonging_classes',
    ontology_path='http://functions.com/parameters#ontologyParam',
    instance_iri='http://functions.com/parameters#instanceParam'
)
def get_belonging_classes(ontology_path: str, instance_iri: str) -> list:
    global ontologies
    if ontology_path not in ontologies.keys():
        g = Graph()
        g.parse(ontology_path)
        ontologies[ontology_path] = g

    ontology = ontologies.get(ontology_path)

    results = list(ontology.query(f"""
               SELECT ?class
               {{ <{instance_iri}> rdf:type ?class }}
        """))
    result_list = []
    for result in results:
        result_list.append(str(result[0]))
    return result_list


if __name__ == '__main__':
    ontology_path = Path(Path(__file__).parent, '../resources/ontologies/CountryPlus.ttl')
    instance_iri = 'https://sws.geonames.org/146669'
    class_iri = 'https://ontology.siemens-energy.com/cbam/EU_Member_State'
    x = belong_to_class(str(ontology_path.absolute()), instance_iri, class_iri)
    print(x)
    instance_iri = 'https://sws.geonames.org/102358'
    x = belong_to_class(str(ontology_path.absolute()), instance_iri, class_iri)
    print(x)
    x = get_belonging_classes(str(ontology_path.absolute()), instance_iri)
    print(x)
