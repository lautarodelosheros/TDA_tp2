from visitante import Visitante

def insertar_ordenado_salidas(lista_salidas, visitante, i = 0):
    j = len(lista_salidas)
    while i < j:
        medio = (i + j) // 2
        if visitante.hora_salida < lista_salidas[medio].hora_salida:
            j = medio
        else:
            i = medio + 1
    lista_salidas.insert(i, visitante)
