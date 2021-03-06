import streamlit as st
import networkx as nx

G = nx.grid_2d_graph(5, 5)  # 5x5 grid

# print the adjacency list
for line in nx.generate_adjlist(G):
    print(line)
# write edgelist to grid.edgelist
nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
# read edgelist from grid.edgelist
H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

#nx.draw(H)
#plt.show()

# K5 = nx.complete_graph(5)
dot = nx.nx_pydot.to_pydot(H)
st.graphviz_chart(dot.to_string())