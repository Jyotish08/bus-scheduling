import networkx as nx


G = nx.Graph()

# Add nodes
for i in dat:
    G.add_node(i["id"])

# Add edges
for i in results:
    if i[2]:  # boolean check
        G.add_edge(i[0], i[1])
  
  

