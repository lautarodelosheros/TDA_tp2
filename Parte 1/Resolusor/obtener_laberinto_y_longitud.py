from cola import *

def obtener_laberinto_y_longitud(grafo, origen, destino):
    padres, orden = BFS(grafo, origen)
    lista_camino = obtener_camino(padres, origen, destino)
    return (lista_camino, orden[destino])

def BFS(grafo, origen):
    visitados = set()
    padres = {}
    orden = {}
    cola = Cola()
    visitados.add(origen)
    padres[origen] = None
    orden[origen] = 1
    cola.encolar(origen)

    while not cola.esta_vacia():
        vertice = cola.desencolar()

        for adyacente in grafo.obtener_adyacentes(vertice):

            if adyacente not in visitados:
                visitados.add(adyacente)
                orden[adyacente] = orden[vertice] + 1
                padres[adyacente] = vertice
                cola.encolar(adyacente)

    return (padres, orden)

def obtener_camino(padres, origen, destino):
    resultado = []
    actual = destino

    while actual != None:
        resultado.append(actual)
        actual = padres[actual]

    resultado.reverse()
    return resultado
