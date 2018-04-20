import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

Ad = np.loadtxt('matrix.txt')
assign = np.loadtxt('assignment.txt')
Gr=nx.from_numpy_matrix(Ad)
color_map = []
for node in Gr:
    if assign[node] == 0:
        color_map.append('red')
    if assign[node] == 1:
        color_map.append('green')
    if assign[node] == 2:
        color_map.append('blue')
    #else: color_map.append('green')      
nx.draw(Gr,node_color = color_map,with_labels = True)
plt.show()