# -*- coding: utf-8 -*-
"""

@author: Jeanphilippe99
"""
import csv
import gdal
import networkx as nx
from pylab import *
import numpy as np

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
c=csv.writer(open("C:/Users/Tiffany/Desktop/CodeProgrammation/fichiercsv/classe2_closeness.csv","w"))
c1=csv.writer(open("C:/Users/Tiffany/Desktop/CodeProgrammation/fichiercsv/classe1_closeness.csv","w"))
c.writerow(["ID","X","Y","closeness centrality"])
c1.writerow(["ID","X","Y","closeness centrality"])
noeuds=list(G2.nodes())
k=1
K=1
superliste=[]
sliste=[]
for (i,j) in noeuds:
    if nx.closeness_centrality(G2,(i,j))>0.041184182830514046 and nx.closeness_centrality(G2,(i,j))<=0.05461726157449445:
        superliste.append([k,i,j,nx.closeness_centrality(G2,(i,j))])
        k+=1
    elif nx.closeness_centrality(G2,(i,j))>0.05461726157449445 and nx.closeness_centrality(G2,(i,j))<=0.08:
        sliste.append([K,i,j,nx.closeness_centrality(G2,(i,j))])
        K+=1
c.writerows(superliste)
c1.writerows(sliste)
#premier groupe=2156
#0.041184182830514046

#0.05461726157449445

#0.0724318186468073

#nx.closeness_centrality(G2,(i,j))>0.041184182830514046 and nx.closeness_centrality(G2,(i,j))<=0.05461726157449445
#^k=9343
#nx.closeness_centrality(G2,(i,j))>0.05461726157449445 and nx.closeness_centrality(G2,(i,j))<=0.08
#K=2666