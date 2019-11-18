import gdal
import networkx as nx
from pylab import *
import numpy as np
import matplotlib as plt

#add this code to display a distribution of clustering coefficient
                
noeuds=list(nx.nodes(G2))
listecc=[]  #liste des clustering coefficients
k=1
listeid=[] # liste des ID des rues
for l in noeuds:
    listecc.append(float(nx.clustering(G2,(l[0],l[1])))) #ajout des clustering coeff dans la liste
    listeid.append(float(k))
    k=k+1
x= np.array(listeid)
listecc.sort(reverse=True)
y = np.array(listecc)
plot(x, y, "o")
title ("Distribution du coefficient de clustering d'ordre 1")
ylabel("coefficient de clustering d'ordre 1")
xlabel("ID des rues")
show()
