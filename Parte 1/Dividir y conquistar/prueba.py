from dyc import crear_laberinto_dyc
import sys

def obtenerParametros():
	
	if (len(sys.argv) != 3):
		raise Exception()
	return [int(sys.argv[1]), int(sys.argv[2])]

def main():

	try:
		parametros = obtenerParametros()
	except:
		print('Faltan parametros, la sintaxis correcta es: laberinto <anchoGrilla> <altoGrilla>.')
		return

	crear_laberinto_dyc(parametros[0], parametros[1])


if __name__ == '__main__':
	main()
