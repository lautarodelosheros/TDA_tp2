#!/usr/bin/env python3

import sys
import os
from visitante import Visitante

def insertar_ordenado_salidas(salidas, visitante, i = 0):
    j = len(salidas)
    while i < j:
        medio = (i + j) // 2
        if visitante.hora_salida < salidas[medio].hora_salida:
            j = medio
        else:
            i = medio + 1
    salidas.insert(i, visitante)

def generar_sospechosos(visitantes, permanencia, archivo):
    cadena = ''
    for visitante in visitantes:
        cadena += visitante.nombre + ','
    cadena += str(permanencia) + "\n"
    print("khe")
    archivo.write(cadena)

def main():
    if len(sys.argv) > 1:
        nombre_del_archivo = sys.argv[1]

        entradas = []
        salidas = []
        visitantes = []

        planilla = open(nombre_del_archivo, "r")
        for linea in planilla.readlines():
            linea_split = linea.split(',')
            visitante = Visitante(*linea_split)
            entradas.append(visitante)
        planilla.close()

        if os.path.exists("sospechosos.txt"):
            os.remove("sospechosos.txt")
        archivo_salida = open("sospechosos.txt", "w+")

        indice_entradas = 0
        indice_salidas = 0
        for i in range(len(entradas) * 2):
            # Si es una entrada
            if len(entradas) > indice_entradas and (len(salidas) == 0 or len(salidas) < indice_salidas or entradas[indice_entradas].hora_entrada <= salidas[indice_salidas].hora_salida):
                visitante = entradas[indice_entradas]
                visitantes.append(visitante)
                insertar_ordenado_salidas(salidas, visitante, indice_salidas)
                indice_entradas += 1
            # Si es una salida
            else:
                visitante = salidas[indice_salidas]
                duracion = visitante.hora_salida - visitantes[0].hora_entrada
                print (str(visitante.hora_salida) +"-" + str(visitantes[0].hora_entrada) + "=" + str(duracion))
                if 40 <= duracion <= 120:
                    if 5 <= len(visitantes) <= 10:
                        generar_sospechosos(visitantes, duracion, archivo_salida)
                visitantes.remove(visitante)
                indice_salidas += 1

        archivo_salida.close()

    else:
        print 'Se necesita el nombre del archivo de visitas como parametro'

main()
