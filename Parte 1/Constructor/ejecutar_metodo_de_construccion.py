from generar_grafo import generar_grafo
from obtener_laberinto import obtener_laberinto
from generar_archivo_salida import generar_archivo_salida
from dyc import crear_laberinto_dyc

def ejecutar_metodo_de_construccion(metodo_de_construccion, largo, ancho):

    if metodo_de_construccion == "dfs":
        grafo, matriz, origen = generar_grafo(largo, ancho)
        arbol_dfs = obtener_laberinto(grafo, origen)
        generar_archivo_salida(arbol_dfs, matriz, largo, ancho)

    else:
        crear_laberinto_dyc(largo, ancho)
