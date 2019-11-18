# -*- coding: utf-8 -*-
"""

@author: JeanPhilippe99
"""
from math import log10
from pylab import *
import numpy as np
import gdal
import networkx as nx
import matplotlib as plt
G1=nx.Graph()
G1=nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//meshp//dual_graph2.shp')

#//////////////////////////////////////////////////// obtention du bon graphe nettoyé et connexe
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

#affichage logarithm (cumulative probability) vs logarithm (connectivity)

liste_deg_sep=[]

dico=nx.average_degree_connectivity(G2) #dictionnaire contenant les degrees comme clé et leur moyenne dans le graphe
log_degree=[] # liste qui contiendra le logarithme de la connectivité
Liste_degree=[]
for key in dico:
    Liste_degree.append(key)
    log_degree.append(log10(key))
    log_degree.sort()
    Liste_degree.sort()
    
    

frequence=nx.degree_histogram(G2) #contient la frequence de chaque degree
prob_degree=[] # liste contiendra le nombre de noeuds de degree k sur le nombre total de noeuds

for i in Liste_degree:
    prob_degree.append(frequence[i]/nx.number_of_nodes(G2))
prob_degree.reverse() #j'inverse la liste pour avoir une probablité 1 lorsque je serai au premier point/ aussi pour être conforme à l'article
log_prob_cumul=[] #liste des probabilités cumulées
k=0
for i in prob_degree:
    k+=i
    log_prob_cumul.append(log10(k))
    
log_prob_cumul.reverse()  
x=np.array(log_degree)  
y=np.array(log_prob_cumul)
plot(x, y, "o:")
title ("log10(cumulative probability) vs log10(connectivity)")
ylabel("log10 (probabilité cumulé)")
xlabel("log10 (connectivité)")
show()