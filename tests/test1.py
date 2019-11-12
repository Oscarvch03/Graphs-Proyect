import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import random
import pylab
from collections import Counter
colores=[]
presas=4
depredadores=6
def events(aristas,colores,col=colores):
    predacion = []
    competencia = []
    muertes = []
    for i in range(len(G.edges())):
        v = aristas[i][0]
        u = aristas[i][1]
        print()
        print("Animales encontrados")
        print(col[v],col[u])
        if(col[v]=="blues" and col[u]=="red" or col[v]=="red" and col[u]=="blue"):
            if((v,u) not in predacion and u not in muertes and v not in muertes):
                predacion.append(aristas[i])
                muertes.append(u)
                muertes.append(v)
                print("predacion")
        if(col[v]=="red" and col[u]=="red"):
            if((v,u) not in competencia and u not in muertes and v not in muertes):
                competencia.append(aristas[i])
                muertes.append(u)
                muertes.append(v)
                print("competencia")
    return predacion, competencia,muertes
def desface(i,muertes):
    desface = 0
    for p in range(len(muertes)):
        if (p<i):
            desface+=1
    return desface
def get_fig(p0,pf,d0,df,col=colores,p=presas,d=depredadores):
    dp = pf-p0
    dd = df-d0
    aristas = [nodes for nodes in G.edges()]
    predacion,competencia,muertes=events(aristas,col)
    if(p0!=pf and d0==df):
        if(dp>0):
            for i in range(dp):
                pos.append((random.randrange(0, 10), random.randrange(0, 10)))
            posiciones = add_vertex(G,dp,pos,col,"blue")
            p=p+1
        else:
            dp=dp*-1
            print("Eventos predacion")
            print(len(predacion))
            if(len(predacion) >= dp):
                for i in range(dp):
                    print("Quitare nodos")
                    print(dp-i)
                    u = predacion[i][0]
                    v = predacion[i][1]
                    print(u,v)
                    if(col[u]=="Azul"):
                        print("matare a: ", u)
                        print(G.nodes())
                        G.remove_node(u)
                        print("Lo mate")
                        print(G.nodes())
                        col = col[:u]+col[u+1:]
                        print("Y lo borre jajajaj")

                    else:
                        print("matare a: ", v)
                        print(G.nodes())
                        G.remove_node(v)
                        print("Lo mate")
                        print(G.nodes())

                        col = col[:v]+col[v+1:]
                        print("Y lo borre jajajaj")
    elif(p0==pf and d0!=df):
        if(dd>0):
            for i in range(dd):
                pos.append((random.randrange(0, 10), random.randrange(0, 10)))
            posiciones = add_vertex(G,dd,pos,col,"red")
            d=d+1
        else:
            dd=dd*-1
            print("Eventos competencia")
            print(len(competencia))
            if(len(competencia) >= dd ):
                for i in range(dd):
                    print("Quitare nodos")
                    print(dd-i)
                    u = competencia[i][0]
                    v = competencia[i][1]
                    print(u,v)
                    d=desface(i,muertes)
                    if(random.randrange(0,2)==0):
                        print("matare a: ", u)
                        print(G.nodes())
                        G.remove_node(u)
                        print("Lo mate")
                        print(G.nodes())
                        print("len col 1 = ",len(col))
                        print(col)
                        col = col[:u-d]+col[u+1-d:]
                        print("Y lo borre jajajaj")
                        print("len col 2 = ",len(col))
                        print(col)
                    else:
                        print("matare a: ", v)
                        print(G.nodes())
                        G.remove_node(v)
                        print("Lo mate")
                        print(G.nodes())
                        print("len col 1 = ",len(col))
                        print(col)
                        col = col[:v-d]+col[v+1-d:]
                        print("Y lo borre jajajaj")
                        print("len col 2 = ",len(col))
                        print(col)

    elif(p0!=pf and d0!=df):
        if(dp>0):
            for i in range(dp):
                pos.append((random.randrange(0, 10), random.randrange(0, 10)))
            posiciones = add_vertex(G,dp,pos,col,"blue")
            p=p+1
        if(dd>0):
            for i in range(dd):
                pos.append((random.randrange(0, 10), random.randrange(0, 10)))
            posiciones = add_vertex(G,dd,pos,col,"red")
            d=d+1
    else:
        posiciones = add_vertex(G,0,pos,col,"green")
    fig = pylab.figure()
    nx.draw(G,nx.get_node_attributes(G,'pos'),node_color=col,with_labels=True, weight=True)
    return fig

delta = 2

def add_vertex(G,nodos,posiciones,colores,color,dr=delta):
    min = len(G.nodes())
    for i in range(min,min+nodos):
        G.add_node(i,pos = posiciones[i])
        colores.append(color)
    posiciones=nx.get_node_attributes(G,'pos')
    add_edges(G,dr)
    return posiciones

def add_edges(G,delta):
    pos=nx.get_node_attributes(G,'pos')
    nodos=G.nodes()
    #print(nodos)
    for i in range(len(G.nodes())-1):
        for j in range(i+1,len(G.nodes())):
            r = ((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**(1/2)
            if(r<delta):
                G.add_edge(i,j,weight = r)
pos=[(1,1),(13,10),(2,5),(9,10),(9,2),(3,2),(7,2),(8,9),(2,1),(10,10)]

G=nx.Graph()

posiciones = add_vertex(G,presas,pos,colores,"blue")
posiciones = add_vertex(G,depredadores,pos,colores,"red")
print("Aristas------------")
print(G.edges(0))
aristas=G.edges(0)
s=[]
for node in aristas:
    s.append(node)
print(s[0][0])
#Out[7]: {1: (1, 1), 2: (2, 2)}
# nx.draw(G,posiciones,node_color=colores,with_labels=True, weight=True)
# plt.show()
# pos.append((7,7))
# pos.append((8,8))
# pos.append((4,4))
# pos.append((5,5))
# pos.append((6,6))
# posiciones=add_vertex(G,2,pos,colores,"red")
# G.remove_node(1)
# color_map =color_map[1:]
# nx.draw(G,posiciones,node_color=colores,with_labels=True, weight=True)
# plt.show()

# pylab.ion()
P=[4,3,2,2,2,1]
D=[6,6,6,2,1,1]
t=[1,2,3,4,5,6]
num_plots = len(t);
for i in range(num_plots):
    if(i!=0):
        fig = get_fig(P[i-1],P[i],D[i-1],D[i])
        fig.canvas.draw()
        pylab.draw()
        plt.pause(2)
        pylab.close(fig)
    else:
        fig = get_fig(P[i],P[i],D[i],D[i])
        fig.canvas.draw()
        pylab.draw()
        plt.pause(2)
        pylab.close(fig)

pylab.show()

plt.show()
