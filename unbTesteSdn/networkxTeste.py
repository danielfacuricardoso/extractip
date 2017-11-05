import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

### 1 - INFORMAR A TOPOLOGIA ATIVA
listaTopologia = []
listaTopologia.append("CTR,R1, 9")
listaTopologia.append("R1, R2, 2")
listaTopologia.append("R1, R3, 4")
listaTopologia.append("R1, R4, 6")
#listaTopologia.append("R2, R4, 2")
listaTopologia.append("R2, H1, 9")
listaTopologia.append("R3, R4, 3")
listaTopologia.append("R3, H2, 9")

G = nx.DiGraph()

### 2 - CARREGAR O OBJETO DO NETWORKX
for linha in listaTopologia:
    maquinaAtual = linha.split(',')
    origem = str(maquinaAtual[0]).strip()
    destino = str(maquinaAtual[1]).strip()
    peso = int(str(maquinaAtual[2]).strip())
    G.add_edges_from([(origem,destino)], weight=peso)
    G.add_edges_from([(destino,origem)], weight=peso)

### 3 - DEFINE ESTILO PARA O CASO DE EXIBIR TOPOLOGIA GRAFICAMENTE
val_map = {'CTR': 1.0, 'H1': 0.5714285714285714, 'H2': 0.0}
values = [val_map.get(node, 0.45) for node in G.nodes()]
edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
red_edges = [('H2','R3'),('H1','R2'),('CTR','R1'),('R3','H2'),('R2','H1'),('R1','CTR')]
edge_colors = ['blue' if not edge in red_edges else 'red' for edge in G.edges()]
pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos, node_color = values, node_size=2500,edge_color=edge_colors,edge_cmap=plt.cm.Reds, with_labels=True)

### 4 - EXIBE MENOR CAMINHO
print(nx.dijkstra_path(G, 'H1', 'H2', weight='weight'))

### 5 - EXIBE TOPOLOGIA GRAFICAMENTE
pylab.show()
