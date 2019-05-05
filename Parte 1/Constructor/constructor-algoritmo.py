import sys
from ejecutar_metodo_de_construccion import ejecutar_metodo_de_construccion

def main():

    if len(sys.argv) == 4:
        metodo_de_construccion = sys.argv[1]
        largo = int(sys.argv[2])
        ancho = int(sys.argv[3])
        ejecutar_metodo_de_construccion(metodo_de_construccion, largo, ancho)

    else:
        print("Se necesitan 4 parámetros")
        exit()

main()
