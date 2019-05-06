from generar_grafo import generar_grafo
from obtener_laberinto_y_longitud import obtener_laberinto_y_longitud
from generar_archivo_salida import generar_archivo_salida

def resolver_laberinto(archivo):
    grafo, matriz, origen, destino, largo, ancho = generar_grafo(archivo)
    lista_camino, longitud = obtener_laberinto_y_longitud(grafo, origen, destino)
    generar_archivo_salida(grafo, matriz, lista_camino, longitud, largo, ancho)
