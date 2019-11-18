# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:20:39 2019

@author: Tiffany
"""

import gdal
import networkx as nx
import matplotlib.pyplot as plt
import csv
G=nx.Graph()
G=nx.read_shp('C://Users//Tiffany//Desktop//CodeProgrammation//dual_graph2.shp')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
for i in list(G.nodes()): 
    if G.degree(i)==1 :         #selection des noeuds i de degree 1
        for j in list(G.neighbors(i)): #liste des voisins de i, qui doit contenir normalement 1 element car le degree est egal a 1 
            if G.degree(j)==1:     #si le degree du voisin j est aussi egale a 1
                G.remove_node(j)    # on supprime i et j
                G.remove_node(i)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


