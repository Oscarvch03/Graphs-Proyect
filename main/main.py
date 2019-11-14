################################################################################
# LIBRERIAS IMPORTADAS #########################################################


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import pylab

import sys
sys.path.insert(0, '../')

from modelo.modelo import xfr, yfr


################################################################################
# DEFINICION DE FUNCIONES Y VARIABLES GLOBALES #################################


colores =[]
muertes = []



def validarCom(competencia, validaciones, muertes):
    competenciaval = []
    muertesTemporales = muertes[:]
    pred = [i for i in range(len(competencia))]
    r = -1
    for i in range(validaciones):
        r = random.choice(pred)
        u = competencia[r][0]
        v = competencia[r][1]
        pred.pop()

        if (u not in muertesTemporales and v not in muertesTemporales):
            competenciaval.append((u,v))
            del competencia[r]
            muertesTemporales.append(u)
            muertesTemporales.append(v)
        else:
            del competencia[r]

    return competenciaval



def validarDep(depredacion, validaciones, muertes):
    depredacionval = []
    muertesTemporales = muertes[:]
    pred = [i for i in range(len(depredacion))]
    r = -1
    for i in range(validaciones):
        r = random.choice(pred)
        u = depredacion[r][0]
        v = depredacion[r][1]
        pred.pop()

        if (u not in muertesTemporales and v not in muertesTemporales):
            depredacionval.append((u,v))
            del depredacion[r]
            muertesTemporales.append(u)
            muertesTemporales.append(v)
        else:
            del depredacion[r]

    return depredacionval



def events(aristas, col, muertes):
    predacion = []
    competencia = []
    for i in range(len(G.edges())):
        u = aristas[i][0]
        v = aristas[i][1]
        dv = desfase(v, muertes)
        du = desfase(u, muertes)

        if ((col[u-du-1] == "blue" and col[v-dv-1] == "red") or (col[u-du-1] == "red" and col[v-dv-1] == "blue")):
            if ((v,u) not in predacion):
                predacion.append(aristas[i])

        if (col[u-du-1] == "red" and col[v-dv-1] == "red"):
            if ((v,u) not in competencia):
                competencia.append(aristas[i])

    return predacion, competencia, muertes



def desfase(i,muertes):
    desfase = 0
    for p in muertes:
        if (p < i):
            desfase += 1
    return desfase



def get_fig(G, p0, pf, d0, df, col, muertes, p, d):
    dp = pf - p0
    dd = df - d0
    aristas = [nodes for nodes in G.edges()]
    predacion, competencia, muertes = events(aristas, col, muertes)

    if (p0 != pf):
        if (dp > 0):
            add_vertex(G, dp, col, "blue")
            p = p + dp
        else:
            dp = dp * -1
            idx = min(len(predacion), dp)
            predacion = validarDep(predacion, idx, muertes)
            for i in range(len(predacion)):
                u = predacion[i][0]
                v = predacion[i][1]
                du = desfase(u, muertes)
                dv = desfase(v, muertes)

                if (col[u-du-1] == "blue"):
                    G.remove_node(u)
                    muertes.append(u)
                    del col[u-du-1]

                else:
                    G.remove_node(v)
                    muertes.append(v)
                    del col[v-dv-1]

    if (d0 != df):
        if (dd > 0):
            add_vertex(G, dd, col, "red")
            d = d + dd
        else:
            dd = dd * -1
            idx = min(dd, len(competencia))
            competencia = validarCom(competencia, idx, muertes)
            for i in range(len(competencia)):
                u = competencia[i][0]
                v = competencia[i][1]
                du = desfase(u, muertes)
                dv = desfase(v, muertes)

                if (random.randrange(0, 2) == 0):
                    G.remove_node(u)
                    muertes.append(u)
                    del col[u-du-1]

                else:
                    G.remove_node(v)
                    muertes.append(v)
                    del col[v-dv-1]

    if (p0 == pf and d0 == df):
        add_vertex(G, 0, col, "green")

    fig = pylab.figure()
    nx.draw(G, nx.get_node_attributes(G, 'pos'), node_color = col, with_labels = True)

    return fig, col



delta = 10



def add_vertex(G, nodos, colo, color, dr=delta):
    min = len(G.nodes())
    max = 0
    for i in G.nodes():
        if (i > max):
            max = i

    for i in range(max + 1, max + 1 + nodos):
        G.add_node(i, pos = (random.randrange(1, 100), random.randrange(1, 100)))
        colo.append(color)

    add_edges(G, dr)



def add_edges(G, delta):
    pos = nx.get_node_attributes(G, 'pos')
    poss = []
    node = []
    for i, j in pos.items():
        node.append(i)
        poss.append(j)

    for i in range(len(poss) - 1):
        for j in range(i + 1, len(poss)):
            r = ((poss[i][0] - poss[j][0]) ** 2 + (poss[i][1] - poss[j][1]) **2 ) ** (1/2)
            if (r < delta and (node[i], node[j]) not in G.edges()):
                G.add_edge(node[i], node[j], weight = r)


################################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################

G = nx.Graph() # Grafo
P = [int(i) for i in xfr] # Presas
D = [int(i) for i in yfr] # Depredadores
t = [i for i in range(1, len(P) + 1)]

Pi = P[0]
Di = D[0]

add_vertex(G, P[0], colores, "blue")
add_vertex(G, D[0], colores, "red")

num_plots = len(t)
n = 1
for i in range(num_plots - 1):
    print("Tiempo =", i)
    # print("Presas:", P[i])
    # print("Depredadores:", D[i])
    # print("Total =", P[i] + D[i])
    # print()

    if(i == 0):
        fig, colores = get_fig(G, P[i], P[i], D[i], D[i], colores, muertes, Pi, Di)
        fig.canvas.draw()
        pylab.draw()
        plt.pause(n)
        pylab.close(fig)
    else:
        fig, colores = get_fig(G, P[i], P[i + 1], D[i], D[i + 1], colores, muertes, Pi, Di)
        fig.canvas.draw()
        pylab.draw()
        # if i == 10:
        #     pylab.savefig("ResultadosGrafo.png")
        #     break
        plt.pause(n)
        pylab.close(fig)

pylab.show()
plt.show()
