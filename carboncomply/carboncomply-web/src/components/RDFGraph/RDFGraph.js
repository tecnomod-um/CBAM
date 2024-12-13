import { React } from "react";
import { graph, parse } from 'rdflib';
import Graph from 'react-graph-vis';
import { v4 as uuidv4 } from 'uuid';
import Box from '@mui/material/Box';
import RDFGraphStyles from './RDFGraph.module.css';

function RDFGraph({ ttlText }) {
    const parseTurtleToVisGraph = (inputText) => {
        console.log("Montando rdf graph");
        var store = graph();
        var mimeType = 'text/turtle'
        const uri = 'https://example.org/resource.ttl';
        parse(inputText, store, uri, mimeType);
        return getVisGraph(store);
    };

    const getVisGraph = (store) => {
        var id = 1;
        var idByIRI = {};
        var nodes = [];
        var edges = [];
        var label;
        var subjectAlreadyPresent = false;
        var objectAlreadyPresent = false;
        store.statements.forEach((triple) => {
            var subjectNode = null;
            var objectNode = null;
            var subject = triple.subject;
            if (subject.termType === 'NamedNode') {
                if (!(subject.value in idByIRI)) {
                    subjectAlreadyPresent = false;
                    idByIRI[subject.value] = id;
                    label = render(subject, store);
                    subjectNode = { id: id, label: label, title: subject.value, group: 'NamedNode' };
                    id = id + 1;
                } else {
                    subjectAlreadyPresent = true;
                    subjectNode = { id: idByIRI[subject.value] };
                }
            }
            var predicate = triple.predicate;
            var object = triple.object;
            if (object.termType === 'NamedNode') {
                if (!(object.value in idByIRI)) {
                    objectAlreadyPresent = false;
                    idByIRI[object.value] = id;
                    label = render(object, store)
                    objectNode = { id: id, label: label, title: object.value, group: 'NamedNode' };
                    id = id + 1;
                } else {
                    objectAlreadyPresent = true;
                    objectNode = { id: idByIRI[object.value] };
                }
            } else if (object.termType === 'Literal') {
                objectAlreadyPresent = false;
                label = justify(object.value);
                objectNode = { id: id, label: label, title: object.value, group: 'Literal' };
                id = id + 1;
            }

            if (subjectNode !== null && objectNode !== null) {
                if (!subjectAlreadyPresent) {
                    nodes.push(subjectNode);
                }
                if (!objectAlreadyPresent) {
                    nodes.push(objectNode);
                }
                var edgeLabel = render(predicate);
                edges.push({ from: subjectNode.id, to: objectNode.id, label: edgeLabel });
            }

        });
        return { nodes: nodes, edges: edges };
    };

    const render = (node) => {
        var iri = node.value;
        return iri.substring(Math.max(iri.lastIndexOf("/") + 1, iri.lastIndexOf("#") + 1));
    };

    const justify = (text) => {
        var max_line_length = 25;
        var justifiedText = '';
        for (let i = 0; i < text.length; i++) {
            if (i%max_line_length === 0) {
            justifiedText = justifiedText + '\n'
            }
            justifiedText = justifiedText + text[i]
        }
        return justifiedText.trim();
    };


    const options = {
        layout: {
            hierarchical: false
        },
        edges: {
            color: "#000000"
        },
        height: "100%",
        physics: {
            enabled: true
        },
        groups: {
            NamedNode: { color: {border: '#714180', background: '#c49bd1'},
                borderWidth: 1, 
                shape: 'ellipsis'
            },
            Literal: {
                color: {border: '#48a341', background: '#8adb84'},
                borderWidth: 1,
                shape: 'box'
            }
        }
    };


    return (
        <Box className={RDFGraphStyles.BoxStyle}>
            <Box style={{ height: '70vh' }}>
                <Graph
                    key={uuidv4()}
                    graph={parseTurtleToVisGraph(ttlText)}
                    options={options}
                //getNetwork={network => {
                //  if you want access to vis.js network api you can set the state in a parent component using this property
                //}}
                />
            </Box>
        </Box>
    );
}


export default RDFGraph;