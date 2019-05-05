from grafo import *

def generar_grafo(largo, ancho):
    matriz = []
    grafo = Grafo(False)
    generar_matriz(matriz, largo, ancho)
    cargar_matriz_y_grafo(matriz, grafo, largo, ancho)
    cargar_aristas(grafo, matriz, largo, ancho)
    return (grafo, matriz, matriz[0][0])

def generar_matriz(matriz, largo, ancho):

    for i in range(largo) :
        fila = [0] * ancho
        matriz.append(fila)

def cargar_matriz_y_grafo(matriz, grafo, largo, ancho):
    i = 0
    j = 0

    for k in range(largo*ancho):

        if j == ancho:
            i += 1
            j = 0

        matriz[i][j] = k
        grafo.agregar_vertice(k)
        j += 1

def cargar_aristas(grafo, matriz, largo, ancho):

    for i in range(largo):

        for j in range(ancho):

            numero = matriz[i][j]
            lista_adyacentes = obtener_adyacentes(matriz, i, j, largo, ancho)
            _cargar_aristas(grafo, numero, lista_adyacentes)


def obtener_adyacentes(matriz, posicion1, posicion2, largo, ancho):
    lista_auxiliar = []

    if posicion1 - 1 >= 0: lista_auxiliar.append(matriz[posicion1 - 1][posicion2])

    if posicion2 - 1 >= 0: lista_auxiliar.append(matriz[posicion1][posicion2 - 1])

    if posicion1 + 1 < largo: lista_auxiliar.append(matriz[posicion1 + 1][posicion2])

    if posicion2 + 1 < ancho: lista_auxiliar.append(matriz[posicion1][posicion2 + 1])

    return lista_auxiliar

def _cargar_aristas(grafo, numero, lista_adyacentes):

    for adyacente in lista_adyacentes:
        grafo.agregar_arista(numero, adyacente)
