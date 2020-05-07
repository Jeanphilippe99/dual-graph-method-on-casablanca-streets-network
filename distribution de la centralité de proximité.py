# -*- coding: utf-8 -*-
"""


@author: Jeanphilippe99
"""

import gdal
import networkx as nx
from pylab import *
import numpy as np

G1 = nx.Graph()
G1 = nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//meshp//dual_graph2.shp')

#//////////////////////////////////////////////////// obtention du bon graphe nettoyé et connexe


k = 0
for i in list(G1.nodes()): 
   if G1.degree(i) == 1 :         #selection des noeuds i de degree 1
      for j in list(G1.neighbors(i)): #liste des voisins de i, qui doit contenir normalement 1 element car le degree est egal a 1 
         if G1.degree(j) == 1:     #si le degree du voisin j est aussi egale a 1
              G1.remove_node(j)    # on supprime i et j
              G1.remove_node(i)
              k+=1
G=nx.Graph.to_undirected(G1)
G2=nx.Graph.to_undirected(G1)

compt=0
noeuds_a_garder=[]
for nv in nx.shortest_path(G,(-7.602920444662278, 33.552537305301016)).keys():
    noeuds_a_garder.append(nv)
    compt+=1

for noeud in noeuds_a_garder:
    G.remove_node(noeud)
for noeud in list(G.nodes()):
    G2.remove_node(noeud)
#////////////////////////////////////////////////////////////////////////////////////cetait le nettoyage du graphe

                


noeuds=list(nx.nodes(G2))
listecloseness=[]  #liste des clustering coefficients
k=1
listeid=[] # liste des ID des rues
for l in noeuds:
    listecloseness.append(float(nx.closeness_centrality(G2,(l[0],l[1])))) #ajout des clustering d'ordre 2 dans la liste
    listeid.append(float(k))
    k=k+1
x= np.array(listeid)
listecloseness.sort(reverse=True)
y = np.array(listecloseness)
plot(x, y, "o")
title ("Distribution de la centralité de proximité")
ylabel("centralité de proximité")
xlabel("ID des rues")
show()
#from math import log10
#nbre_classe=3
#raison=10**((log10(max(listecloseness))-log10(min(listecloseness)))/nbre_classe)
#print("la raison est",raison)
