import json
import os
from graphviz import Digraph

file = "/home/hutu/PersonaDataset/AMRBART/examples/persona_amr_graph.json"
with open(file, 'r') as f:
    graphs = json.load(f)

graph = graphs[12]

dot = Digraph(comment='The Test Table')
node_set = []
for triple in graph:
    if triple[0] not in node_set:
        dot.node(triple[0],triple[2])
        node_set.append(triple[0])
    elif triple[2][0] != 'z':
        dot.node(triple[2], triple[2])
        dot.edge(triple[0],triple[2],triple[1])
    else:
        dot.edge(triple[0],triple[2],triple[1])

print(dot.source)

