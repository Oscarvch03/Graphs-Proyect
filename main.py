import networkx as  nx
import matplotlib.pyplot as plt
# class presa():
#     def __init__(self,tsc)

def add_vertex(G,presas,depredadores):
    G.add_nodes_from([presas[i] for i in range(len(presas))])
    G.add_nodes_from([depredadores[i] for i in range(len(depredadores))])
def add_edges(G,aristas):
    G.add_edges_from([i for i in aristas])
G=nx.Graph()
add_vertex(G,[x for x in range(7)],[y for y in range(7,16)])
add_edges(G,[(7,6),(8,9),(6,5),(5,9),(8,7),(2,7),(1,6),(0,5),(4,9),(3,8),(13,2),(13,3),(14,3),(15,4),(10,0),(11,1),(12,2)])
#G.add_edge(1,2)
l=G.number_of_nodes()
s=G.number_of_edges()
print(l)
print(list(G.nodes))
print(s)
print(G.edges)
options = {
     'nodes_color': ["red","lightblue"],
     'nodes_size': 150,
     'width': 1,
}


plt.subplot(111)

#nx.draw_spectral(G, **options,with_labels=False, font_weight='bold')
nx.draw_shell(G,nlist=[range(5,10),range(5), range(10,16)],with_labels=True, font_weight='bold')
#nx.draw_circular(G, **options,with_labels=False, font_weight='bold')
#nx.draw_random(G, **options,with_labels=False, font_weight='bold')
plt.savefig("grafoEjemplo.PNG")
plt.show()
