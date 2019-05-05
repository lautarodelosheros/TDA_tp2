def generar_archivo_salida(arbol_dfs, matriz, largo, ancho):
    with open("mapa-laberinto.txt", "w") as archivo_salida:
        borde_superior = "+ " + "+-"*(ancho - 1) + "+\n"
        borde_inferior = "+-"*(ancho - 1) + "+ " + "+\n"
        archivo_salida.write(borde_superior)

        for i in range(largo):
            lista_horizontales = []
            lista_verticales = []

            for j in range(ancho):
                actual = matriz[i][j]
                lista_adyacentes = arbol_dfs.obtener_adyacentes(actual)
                ubicar_paredes_verticales(matriz, lista_adyacentes, lista_verticales, i, j, archivo_salida, ancho)
                ubicar_paredes_horizontales(matriz, lista_adyacentes, lista_horizontales, i, j, archivo_salida, ancho, largo)

            archivo_salida.write( "".join(lista_verticales) )

            if i + 1 == largo: archivo_salida.write(borde_inferior)

            else: archivo_salida.write( "".join(lista_horizontales) )

def ubicar_paredes_verticales(matriz, lista_adyacentes, lista_verticales, posicion1, posicion2, archivo_salida, ancho):

    if not es_adyacente_horizontal(posicion1, posicion2 - 1, matriz, lista_adyacentes): lista_verticales.append("|")

    else: lista_verticales.append(" ")

    lista_verticales.append(" ")

    if posicion2 + 1 >= ancho: lista_verticales.append("|\n")

def es_adyacente_horizontal(posicion1, posicion2, matriz, lista_adyacentes):

    if posicion2 < 0: return False

    if matriz[posicion1][posicion2] in lista_adyacentes: return True

    return False

def ubicar_paredes_horizontales(matriz, lista_adyacentes, lista_horizontales, posicion1, posicion2, archivo_salida, ancho, largo):
    lista_horizontales.append("+")

    if not es_adyacente_vertical(posicion1 + 1, posicion2, largo, matriz, lista_adyacentes): lista_horizontales.append("-")

    else: lista_horizontales.append(" ")

    if posicion2 + 1 >= ancho: lista_horizontales.append("+\n")

def es_adyacente_vertical(posicion1, posicion2, largo, matriz, lista_adyacentes):

    if posicion1 >= largo: return False

    if matriz[posicion1][posicion2] in lista_adyacentes: return True

    return False
