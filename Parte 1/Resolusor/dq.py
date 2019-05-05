import sys
from resolver_laberinto import resolver_laberinto

def main():

    if len(sys.argv) == 2:
        archivo = sys.argv[1]
        resolver_laberinto(archivo)

    else:
        print("Se necesitan 2 parámetros")
        exit()

main()
