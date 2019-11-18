# -*- coding: utf-8 -*-
"""
@author: Jeanphilippe99
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:13:08 2019

@author: Tiffany
"""
import gdal
import networkx as nx
from math import log10
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

#création de la fonction de clustering d'ordre 2
def degree_ordre_2(G,noeud):
    voisin=[] #cette liste contiendra tous les noeuds voisin d'ordre 2 du point entrée y compris lui même
    vois_sans_doublon=[]
    voisin=list(G.neighbors(noeud))
    for nod in list(G.neighbors(noeud)):
        voisin+=list(G.neighbors(nod))  #je remplis ma liste
    vois_sans_doublon=list(set(voisin))    # je supprime les doublons
    vois_sans_doublon.remove(noeud)   #je supprime le noeuds lui même
    return len(vois_sans_doublon)
    

def lien_ordre_2(G,noeud):# fonction pour calculer le nombre d'arc entre les voisins jusqu'à l'ordre 2
    voisin=[]
    voisin_voisin=[]
    k=0
    K=0
    for nod in list(G.neighbors(noeud)):
        voisin+=list(G.neighbors(nod)) #je regroupe tous les voisins des noeuds dans une liste
        for nodnod in list(G.neighbors(nod)):
            if nodnod==noeud:
                voisin_voisin+=[]
            else:
                voisin_voisin+=list(G.neighbors(nodnod))
            if noeud in voisin_voisin:
                for i in range(0,voisin_voisin.count(noeud)):
                    voisin_voisin.remove(noeud)
    for nod in list(G.neighbors(noeud)):
        for i in range(0,voisin_voisin.count(nod)):
            voisin_voisin.remove(nod)
        for nde in voisin_voisin:
            if voisin_voisin.count(nde)>4:
                K+=voisin_voisin.count(nde)/2
    if K%2==0:
       var=K
    else:
       var=K+1
    for i in range(0,voisin.count(noeud)): #je retire le noeuds en questions dans la liste
        voisin.remove(noeud)
    for i in  list(G.neighbors(noeud)):
        if i in voisin:
            k+=voisin.count(i)           #je verifie le nombre de fois que les voisins apparaissent dans la liste
        else:
            k+=0
    if (k % 2) ==0:
       return len(voisin)-k//2    # pour pouvoir comprendre la fonction prend un stylo et une feuille et gratte parce que jai refléchis et je ne sais pas comment te l'expliquer
    else:
       return len(voisin)-k//2-1  # de toute façon ça marche et c'est l'essentiel lol

def clustering_ordre_2(G,x):
    return (2*lien_ordre_2(G,x))/(degree_ordre_2(G,x)*(degree_ordre_2(G,x)-1))                
#//////////////////////////////////////////////////////////////fin de le création de la fonction

noeuds=list(nx.nodes(G2))
listecc2=[]  #liste des clustering coefficients d'ordre 2
k=1
listeid=[] # liste des ID des rues
for l in noeuds:
    listecc2.append(float(clustering_ordre_2(G2,(l[0],l[1])))) #ajout des clustering d'ordre 2 dans la liste
    listeid.append(float(k))
    k=k+1
#listecc2.sort(reverse=True)
nbre_classe=3
raison=10**((log10(max(listecc2))-log10(min(listecc2)))/nbre_classe)
print("la raison est",raison)

