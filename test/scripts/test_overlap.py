import json
import networkx as nx
def is_overlap(r1, r2,gap=0):
    return not (r1["end_min"] + gap <= r2["start_min"] or r2["end_min"] + gap <= r1["start_min"])

with open("data/sample_route.json",'r') as file:
  dat = json.load(file)
d=list()
for i in dat:
  a,b=i["start"].split(":")
  t=int(a)*60+int(b)
  i["start_min"]=t
  a,b=i["end"].split(":")
  t=int(a)*60+int(b)
  i["end_min"]=t
dat.sort(key=lambda r: r["start_min"])
results = []

for i in range(len(dat)):
    for j in range(i + 1, len(dat)):
        r1 = dat[i]
        r2 = dat[j]

        overlap = is_overlap(r1, r2, 10)

        results.append((r1["id"], r2["id"], overlap))


G = nx.Graph()

# Add nodes
for i in dat:
    G.add_node(i["id"])

# Add edges
for i in results:
    if i[2]:  # boolean check
        G.add_edge(i[0], i[1])
coloring_dict = nx.greedy_color(G, strategy='largest_first')
node_colors = [(node,coloring_dict[node]) for node in G.nodes()]
print("\nBus Assignments:")
for node in coloring_dict:
    print(f"{node} → Bus {coloring_dict[node] + 1}")
print("\nNodes:", list(G.nodes()))
print("Edges:", list(G.edges()))
  
  
