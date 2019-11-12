import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import pylab
# from collections import Counter


from testmodelo import xfr, yfr


colores =[]
muertes = []

presas=6
depredadores=8

# def restar(lista,num):
#     s = []
#     for i in lista:
#         if(i!=num):
#             s.append(i)
#     return s
def validarCom(competencia,validaciones,muertes):
    competenciaval = []
    muertesTemporales = muertes[:]
    pred = [i for i in range(len(competencia))]
    r=-1
    for i in range(validaciones):


        r = random.choice(pred)



        u = competencia[r][0]
        v = competencia[r][1]
        pred.pop()
        if(u not in muertesTemporales and v not in muertesTemporales):
            competenciaval.append((u,v))

            del competencia[r]

            muertesTemporales.append(u)
            muertesTemporales.append(v)
        else:
            del competencia[r]
    return competenciaval

def validarDep(depredacion,validaciones,muertes):
    depredacionval = []
    muertesTemporales = muertes[:]
    pred = [i for i in range(len(depredacion))]
    r=-1
    for i in range(validaciones):
        r = random.choice(pred)
        u = depredacion[r][0]
        v = depredacion[r][1]
        pred.pop()
        if(u not in muertesTemporales and v not in muertesTemporales):
            depredacionval.append((u,v))
            del depredacion[r]
            muertesTemporales.append(u)
            muertesTemporales.append(v)
        else:
            del depredacion[r]
    return depredacionval

def events(aristas,col,muertes):
    predacion = []
    competencia = []
    for i in range(len(G.edges())):
        u = aristas[i][0]
        v = aristas[i][1]
        dv=desfase(v,muertes)
        du=desfase(u,muertes)
        # print(col)
        # print(len(col))
        # print(u,du,v,dv)
        if((col[u-du-1]=="blue" and col[v-dv-1]=="red") or (col[u-du-1]=="red" and col[v-dv-1]=="blue")):
            if((v,u) not in predacion):
                predacion.append(aristas[i])

        if(col[u-du-1]=="red" and col[v-dv-1]=="red"):
            if((v,u) not in competencia):
                competencia.append(aristas[i])

    return predacion, competencia,muertes
def desfase(i,muertes):
    desfase = 0
    for p in muertes:
        if (p<i):
            desfase+=1
    return desfase

def get_fig(G, p0,pf,d0,df,col,muertes,p=presas,d=depredadores):
    dp = pf-p0
    dd = df-d0
    aristas = [nodes for nodes in G.edges()]
    #print(G.edges())
    #print("-----------",aristas)
    predacion,competencia,muertes=events(aristas,col,muertes)
    if(p0!=pf):
        if(dp>0):
            add_vertex(G,dp,col,"blue")
            p=p+dp
        else:
            dp=dp*-1
            idx = min(len(predacion),dp)
            predacion = validarDep(predacion,idx,muertes)
            for i in range(len(predacion)):

                u = predacion[i][0]
                v = predacion[i][1]

                du=desfase(u,muertes)
                dv=desfase(v,muertes)


                # print("Color INICIAL")
                # print(col)
                # print(len(col))

                if(col[u-du-1]=="blue"):


                    G.remove_node(u)
                    muertes.append(u)


                    # print("------------------------------")
                    # print(col[u-du],u-du)
                    del col[u-du-1]
                    # print("------------------------------")

                else:

                    G.remove_node(v)
                    muertes.append(v)


                    # print("------------------------------")
                    #
                    # print(col[v-dv-1],v-dv-1)

                    del col[v-dv-1]
                    # print("------------------------------")

                # print("Color final")
                # print(col)
                # print(len(col))
    if(d0!=df):
        if(dd>0):
            add_vertex(G,dd,col,"red")
            d=d+dd
        else:
            dd=dd*-1

            idx = min(dd,len(competencia))
            competencia = validarCom(competencia,idx,muertes)
            for i in range(len(competencia)):


                u = competencia[i][0]
                v = competencia[i][1]

                du=desfase(u,muertes)
                dv=desfase(v,muertes)
                if(random.randrange(0,2)==0):

                    G.remove_node(u)
                    muertes.append(u)
                    del col[u-du-1]
                else:
                    G.remove_node(v)
                    muertes.append(v)
                    del col[v-dv-1]
    if(p0==pf and d0==df):
        add_vertex(G,0,col,"green")
    fig = pylab.figure()
    # print("0000000000000000000000000000")
    # print(nx.get_node_attributes(G,'pos'))
    # print(len(nx.get_node_attributes(G,'pos')))
    # print(col)
    # print(len(col))
    # print(G.nodes())
    # print(len(G.nodes()))
    # print("0000000000000000000000000000")

    nx.draw(G,nx.get_node_attributes(G,'pos'),node_color=col,with_labels=True)
    return fig,col
delta = 20
def add_vertex(G,nodos,colo,color,dr=delta):
    min = len(G.nodes())
    # print("///////////////////////////////////////////////////////////////////////")
    # print()
    # print("INICIAL")

    # print(nx.get_node_attributes(G,'pos'))
    # print(len(nx.get_node_attributes(G,'pos')))
    #
    # print(colo)
    # print(len(colo))
    max=0
    for i in G.nodes():
        if(i>max):
            max=i
    # print(G.nodes())
    # print("El maximo es :",max)
    # print(max+nodos)
    for i in range(max+1,max+1+nodos):
        G.add_node(i,pos = (random.randrange(1,100),random.randrange(1,100)))
        colo.append(color)
    # print("Final")
    # print(nx.get_node_attributes(G,'pos'))
    # print(len(nx.get_node_attributes(G,'pos')))
    # print(colo)
    # print(len(colo))

    add_edges(G,dr)
def add_edges(G,delta):
    pos=nx.get_node_attributes(G,'pos')
    poss=[]
    node=[]
    for i,j in pos.items():
        node.append(i)
        poss.append(j)
    for i in range(len(poss)-1):
        for j in range(i+1,len(poss)):
            r = ((poss[i][0]-poss[j][0])**2+(poss[i][1]-poss[j][1])**2)**(1/2)
            if(r<delta and (node[i],node[j]) not in G.edges()):
                G.add_edge(node[i],node[j], weight = r)



# add_vertex(G,presas,colores,"blue")
# add_vertex(G,depredadores,colores,"red")
# P=[presas,6,8,10,3,2,5,6]
# D = [depredadores,7,10,3,12,4,8]
# t=[1,2,3,4,5,6,7]

G=nx.Graph()
P = [int(i) for i in xfr]
D = [int(i) for i in yfr]
t = [i for i in range(1, len(P) + 1)]

add_vertex(G,P[0], colores,"blue")
add_vertex(G,D[0],colores,"red")



num_plots = len(t);
for i in range(num_plots-1):
    print("Tiempo =", i)
    print("Presas:", P[i])
    print("Depredadores:", D[i])
    print("Total =", P[i] + D[i])
    print()
    if(i==0):
        fig,colores = get_fig(G, P[i],P[i],D[i],D[i],colores,muertes)
        # print("-0-0-0-0-00--00-0-0-0-0-0-0-00--000-0-00-0-0-00-0")
        # print(colores)
        # print(len(colores))
        # print("-0-0-0-0-00--00-0-0-0-0-0-0-00--000-0-00-0-0-00-0")
        fig.canvas.draw()
        pylab.draw()
        plt.pause(10)
        pylab.close(fig)
    else:
        fig,colores = get_fig(G, P[i],P[i+1],D[i],D[i+1],colores,muertes)
        # print("-0-0-0-0-00--00-0-0-0-0-0-0-00--000-0-00-0-0-00-0")
        # print(colores)
        # print(len(colores))
        # print("-0-0-0-0-00--00-0-0-0-0-0-0-00--000-0-00-0-0-00-0")
        fig.canvas.draw()
        pylab.draw()
        plt.pause(10)
        pylab.close(fig)

pylab.show()
plt.show()
