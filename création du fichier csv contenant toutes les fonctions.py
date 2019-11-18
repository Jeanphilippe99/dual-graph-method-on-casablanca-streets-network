# -*- coding: utf-8 -*-
"""


@author: Jeanphilippe99
"""

import gdal
import networkx as nx
import matplotlib as plt
import csv
G1=nx.Graph()
G1=nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//meshp//dual_graph2.shp')

#//////////////////////////////////////////////////// obtention d'un graphe nettoyé et connexe
def degree_separation(G, x):  #création d'une fonction qui permettra de calculer le degree de separation moyen d'un noeuds. la fonction prend en parametre un dictionnaire
   deg=0
   for i in nx.shortest_path(G,x).values():
       deg+=len(i)-1    #chaque i est un tableau contenant le chemin à partir de x jusqu'à chaque point
   return deg/nx.number_of_nodes(G)


k=0
for i in list(G1.nodes()): 
   if G1.degree(i)==1 :         #selection des noeuds i de degree 1
      for j in list(G1.neighbors(i)): #liste des voisins de i, qui doit contenir normalement 1 element car le degree est egal a 1 
         if G1.degree(j)==1:     #si le degree du voisin j est aussi egale a 1
              G1.remove_node(j)    # on supprime i et j
              G1.remove_node(i)
              k+=1
# cette étape va consister à rendre notre graphe nettoyé connexe              
G=nx.Graph.to_undirected(G1)
G2=nx.Graph.to_undirected(G1)

compt=0
noeuds_a_garder=[]
for nv in nx.shortest_path(G,(-7.602920444662278, 33.552537305301016)).keys():# ces points ont été choisis car lors d'une visualisation, on a remarqué qu'une bonne partie des noeuds du réseau passait par ces points
    noeuds_a_garder.append(nv)
    compt+=1

for noeud in noeuds_a_garder:
    G.remove_node(noeud)
for noeud in list(G.nodes()):
    G2.remove_node(noeud)
#////////////////////////////////////////////////////////////////////////////////////cetait le nettoyage du graphe

# ici l'on va insérer nos calculs dans un fichier csv

c=csv.writer(open("C:/Users/Tiffany/Desktop/CodeProgrammation/Resultat_Fonction.csv","w"))
c.writerow(["ID","X","Y","DEGREE","clustering_coefficient","closeness_centrality"])
noeuds=list(nx.nodes(G2))
k=1
superliste=[]
for l in noeuds:
    superliste.append([k,l[0],l[1],nx.degree(G2,(l[0],l[1])),nx.clustering(G2,(l[0],l[1])),nx.closeness_centrality(G2,(l[0],l[1]))])
    k=k+1
c.writerows(superliste)

print("fini")