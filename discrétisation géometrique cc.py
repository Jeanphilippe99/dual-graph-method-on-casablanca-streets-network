# -*- coding: utf-8 -*-
"""

@author: Jeanphilippe99
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 03:25:32 2019

@author: Tiffany
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:13:08 2019

@author: Tiffany
"""
import gdal
from math import log10
import networkx as nx
G1=nx.Graph()
G1=nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//meshp//dual_graph2.shp')

#//////////////////////////////////////////////////// obtention du bon graphe nettoyé et connexe


k=0
for i in list(G1.nodes()): 
   if G1.degree(i)==1 :         #selection des noeuds i de degree 1
      for j in list(G1.neighbors(i)): #liste des voisins de i, qui doit contenir normalement 1 element car le degree est egal a 1 
         if G1.degree(j)==1:     #si le degree du voisin j est aussi egale a 1
              G1.remove_node(j)    # on supprime i et j
              G1.remove_node(i)
              k+=1
Gx=nx.Graph.to_undirected(G1)
G=nx.Graph.to_undirected(G1)

compt=0
noeuds_a_garder=[]
for nv in nx.shortest_path(Gx,(-7.602920444662278, 33.552537305301016)).keys():
    noeuds_a_garder.append(nv)
    compt+=1

for noeud in noeuds_a_garder:
    Gx.remove_node(noeud)
for noeud in list(Gx.nodes()):
    G.remove_node(noeud)
#////////////////////////////////////////////////////////////////////////////////////cetait le nettoyage du graphe

             
noeuds=list(nx.nodes(G))
listecc=[]  #liste des clustering coefficients d'ordre 2
k=1
listeid=[] # liste des ID des rues
for l in noeuds:
    listecc.append(float(nx.clustering(G,(l[0],l[1])))) #ajout des clustering dans la liste
    listeid.append(float(k))
    k=k+1

nbre_classe=7
raison=10**((log10(max(listecc)))/nbre_classe)
print("la raison est",raison)

