import streamlit as st
import json

from core.graph_builder import build_graph
from core.coloring import assign_buses
from main import load_and_prepare_data  # or adjust if needed

st.title("🚌 Bus Scheduling Optimizer")

# Input JSON
routes_input = st.text_area("Enter routes (JSON format):")

gap = st.number_input("Minimum gap between routes (minutes):", min_value=0, value=10)

if st.button("Optimize"):
    try:
        routes = json.loads(routes_input)

        # Convert + prepare
        for r in routes:
            a, b = r["start"].split(":")
            r["start_min"] = int(a) * 60 + int(b)

            a, b = r["end"].split(":")
            r["end_min"] = int(a) * 60 + int(b)

        routes.sort(key=lambda x: x["start_min"])

        # Build graph + color
        G = build_graph(routes, gap)
        coloring_dict, num_buses = assign_buses(G)

        st.subheader("Results")
        st.write("Total buses required:", num_buses)

        st.write("Bus Assignments:")
        for node in coloring_dict:
            st.write(f"{node} → Bus {coloring_dict[node] + 1}")

    except Exception as e:
        st.error(f"Error: {e}")
