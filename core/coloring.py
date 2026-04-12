
coloring_dict = nx.greedy_color(G, strategy='largest_first')
node_colors = [(node,coloring_dict[node]) for node in G.nodes()]
print("\nBus Assignments:")
for node in coloring_dict:
    print(f"{node} → Bus {coloring_dict[node] + 1}")

  
  

