#!/usr/bin/env python3

import sys
from visitante import Visitante
from merge_sort import merge_sort_por_hora_salida

def generar_sospechosos(visitantes):
    print('SOSPECHOSOS: ')
    for visitante in visitantes:
        print(visitante.nombre + ',' + str(visitante.permanencia))

def main():
    if len(sys.argv) > 1:
        nombre_del_archivo = sys.argv[1]

        entradas = []
        salidas = []
        visitantes = []

        archivo = open(nombre_del_archivo)
        for linea in archivo.readlines():
            linea_split = linea.split(',')
            visitante = Visitante(*linea_split)
            entradas.append(visitante)

        archivo.close()

        indice_entradas = 0
        indice_salidas = 0
        for i in range(len(entradas) * 2):
            # Si es una entrada
            if len(entradas) > indice_entradas and (len(salidas) == 0 or len(salidas) < indice_salidas or entradas[indice_entradas].hora_entrada <= salidas[indice_salidas].hora_salida):
                visitante = entradas[indice_entradas]
                visitantes.append(visitante)
                salidas.append(visitante)
                merge_sort_por_hora_salida(salidas)
                indice_entradas += 1
            # Si es una salida
            else:
                visitante = salidas[indice_salidas]
                if 40 <= visitante.hora_salida - visitantes[0].hora_entrada <= 120:
                    if 5 <= len(visitantes) <= 10:
                        generar_sospechosos(visitantes)
                visitantes.remove(visitante)
                indice_salidas += 1

    else:
        print 'Se necesita el nombre del archivo de visitas como parametro'

main()
