from grafo import *

def generar_grafo(archivo):
    matriz = []
    grafo = Grafo(False)
    largo, ancho = generar_matriz(matriz, archivo)
    cargar_matriz_y_grafo(matriz, grafo, largo, ancho)
    cargar_aristas(grafo, matriz, archivo, largo, ancho)
    return (grafo, matriz, matriz[0][0], matriz[largo - 1][ancho - 1], largo, ancho)

def generar_matriz(matriz, archivo):
    with open(archivo) as archivo_entrada:
        lista_borde_superior = archivo_entrada.readline().rstrip("\n").split("+")
        ancho = len(lista_borde_superior) - 2
        largo = 0

        for linea in archivo_entrada:
            linea_auxiliar = linea.rstrip("\n")

            for caracter in linea_auxiliar:

                if caracter == "+": break

                largo += 1
                fila = [0] * ancho
                matriz.append(fila)
                break

        return (largo, ancho)

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

def cargar_aristas(grafo, matriz, archivo, largo, ancho):
    with open(archivo) as archivo_entrada:
        archivo_entrada.readline()

        for i in range(largo):
            linea_pipe = archivo_entrada.readline().rstrip("\n")
            linea_mas = archivo_entrada.readline().rstrip("\n")

            for j in range(ancho):
                agregar_adyacente_horizontal(grafo, matriz, linea_pipe, i, j)

                if i + 1 == largo: continue

                agregar_adyacente_vertical(grafo, matriz, linea_mas, i, j)

def agregar_adyacente_horizontal(grafo, matriz, linea_pipe, posicion1, posicion2):
    n = (2 * posicion2) + 1

    if linea_pipe[n - 1] != "|": grafo.agregar_arista(matriz[posicion1][posicion2], matriz[posicion1][posicion2 - 1])

def agregar_adyacente_vertical(grafo, matriz, linea_mas, posicion1, posicion2):
    n = (2 * posicion2) + 1

    if linea_mas[n] != "-": grafo.agregar_arista(matriz[posicion1][posicion2], matriz[posicion1 + 1][posicion2])
