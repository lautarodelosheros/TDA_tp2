import random
from grafo import *

def obtener_laberinto(grafo, origen):
    visitados = set()
    arbol_dfs = Grafo(False)

    for vertice in grafo:
        arbol_dfs.agregar_vertice(vertice)

    DFS(grafo, arbol_dfs, origen, visitados)
    return arbol_dfs

def DFS(grafo, arbol_dfs, vertice, visitados):
    visitados.add(vertice)
    lista_adyacentes = grafo.obtener_adyacentes(vertice)
    random.shuffle(lista_adyacentes)

    for adyacente in lista_adyacentes:

        if adyacente not in visitados:
            arbol_dfs.agregar_arista(vertice, adyacente)
            DFS(grafo, arbol_dfs, adyacente, visitados)
