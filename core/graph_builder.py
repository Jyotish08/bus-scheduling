import networkx as nx
from core.overlap import is_overlap

def build_graph(dat, gap=0):
    G = nx.Graph()

    # Add nodes
    for route in dat:
        G.add_node(route["id"])

    # Add edges directly (no results list)
    for i in range(len(dat)):
        for j in range(i + 1, len(dat)):
            r1 = dat[i]
            r2 = dat[j]

            if is_overlap(r1, r2, gap):
                G.add_edge(r1["id"], r2["id"])

    return G
