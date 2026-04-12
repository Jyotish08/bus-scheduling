import networkx as nx

def assign_buses(G, strategy='largest_first'):
    coloring_dict = nx.greedy_color(G, strategy=strategy)

    # Calculate number of buses
    num_buses = max(coloring_dict.values()) + 1

    return coloring_dict, num_buses
