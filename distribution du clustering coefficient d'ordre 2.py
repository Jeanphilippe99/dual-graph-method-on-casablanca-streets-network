# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 00:13:08 2019

@author: Tiffany
"""
import gdal
import networkx as nx
from pylab import *
import numpy as np
import matplotlib as plt
G1=nx.Graph()
G1=nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//meshp//dual_graph2.shp')



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
#fin de le création de la fonction

#affichage de la distribution du clustering coefficient d'ordre 2
noeuds=list(nx.nodes(G2))
listecc=[]  #liste des clustering coefficients
k=1
listeid=[] # liste des ID des rues
for l in noeuds:
    listecc.append(float(clustering_ordre_2(G2,(l[0],l[1])))) #ajout des clustering d'ordre 2 dans la liste
    listeid.append(float(k))
    k=k+1
x= np.array(listeid)
listecc.sort(reverse=True)
y = np.array(listecc)
plot(x, y, "o")
title ("Distribution du coefficient de clustering d'ordre 2")
ylabel("coefficient de clustering d'ordre 2")
xlabel("ID des rues")
show()
