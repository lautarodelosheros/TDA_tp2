import sys
import random
import math

VERTICAL = 0
HORIZONTAL = 1

listaOrientaciones = [VERTICAL, HORIZONTAL]

#Crea la matriz que contendra el laberinto (inicialmente esta vacia).
def crearMatriz(filas, columnas):
	
	return [[' ' for x in range(filas)] for y in range(columnas)] 

#Los parametros se ajustan al modelo de que las paredes son infinitesimales
#entonces el laberinto tiene tantas filas y columnas como las indicadas pero
#como no se pueden dibujar paredes infinitesimales se agregan filas y columnas
#para poder dibujarlas.
def obtenerParametros():
	
	if (len(sys.argv) != 3):
		raise Exception()
	return [2*int(sys.argv[1])-1, 2*int(sys.argv[2])-1]

#Utiliza un criterio euristico para determinar la orientacion de la pared.
#Es el mejor metodo encontrado por nosotros para tener mejor distribucion de paredes.
def determinarOrientacionPared(ancho, alto):
	
	if(ancho > alto):
		return VERTICAL
	elif(alto > ancho):
		return HORIZONTAL
	else:
		return random.choice(listaOrientaciones)

#Determina la posicion mas cercana al centro de la habitacion que sea impar
def determinarCentroImpar(dimension):
	mitad = dimension / 2
	pisoMitad = int(math.floor(mitad))

	if (pisoMitad % 2 == 1):
		return pisoMitad
	elif (abs(pisoMitad + 1 - mitad) < abs(pisoMitad - 1 - mitad)):
		return pisoMitad + 1
	else:
		return pisoMitad - 1 
	

#La idea es que la pared este en el centro de la habitacion.
#Notas que x e y son siempre pares.
def determinarPosicionInicialPared(x, y, ancho, alto, orientacion):

	if (orientacion == VERTICAL):
		xPared = x + determinarCentroImpar(ancho)
		yPared = y
	else:
		xPared = x
		yPared = y + determinarCentroImpar(alto)

	return [xPared, yPared]


def determinarPosicionPuerta(posicionInicialX, posicionInicialY, ancho, alto, orientacion):

	if (orientacion == VERTICAL):
		posicionXPuerta = posicionInicialX
		posicionYPuerta = posicionInicialY + random.choice(range(0, alto - 1, 2))
	else:
		posicionXPuerta = posicionInicialX + random.choice(range(0, ancho - 1, 2))
		posicionYPuerta = posicionInicialY

	return [posicionXPuerta, posicionYPuerta]
	
def determinarLargoPared(ancho, alto, orientacion):
	
	if (orientacion == VERTICAL):
		return alto
	else:
		return ancho

#Basado en la posiciona a escribir de la matriz se determina que simbolo usar para la pared o puerta. 
def caracterRelleno(x, y, posicionPuerta, orientacion):
	
	if(x == posicionPuerta[0] and y == posicionPuerta[1]):
		return ' '

	if(x % 2 != 0 and y % 2 != 0):
		return '+'

	if (orientacion == VERTICAL):
		return '|'
	else:
		return '-'

#Usando para el marco del laberinto los mismos simbolos que para las paredes
#hace que se vea mucho mejor. 
def determinarSimboloMarco(fila):
	if(fila % 2 == 0):
		return '|'
	return '+'

def imprimirLaberinto(matriz, ancho, alto):

	archivo = open('mapa-laberinto.txt', 'w')

	archivo.write('+-' * int(math.ceil((ancho + 2) / 2)))
	archivo.write('+\n')


	for i in range(alto):
		marco = determinarSimboloMarco(i)

		#Determina si es puerta de entrada o marco del laberinto.
		archivo.write(' ' if (i == 0) else marco)

		for j in range(ancho):
			archivo.write(matriz[i][j])

		#Determina si es puerta de salida o marco del laberinto.
		archivo.write(' ' if (i == alto - 1) else marco)

		archivo.write('\n')

	archivo.write('+-' * int(math.ceil((ancho + 2) / 2)))
	archivo.write('+\n')

def ponerPared(matriz, x, y, ancho, alto):

	if (ancho < 2 or alto < 2):
		return;

	orientacion = determinarOrientacionPared(ancho, alto)
	posicionInicial = determinarPosicionInicialPared(x, y, ancho, alto, orientacion)
	posicionPuerta = determinarPosicionPuerta(posicionInicial[0], posicionInicial[1], ancho, alto, orientacion)	
	largoPared = determinarLargoPared(ancho, alto, orientacion)

	xRellenar = posicionInicial[0]
	yRellenar = posicionInicial[1]

	#Guardar pared en la matriz

	for i in range(largoPared):
		if(matriz[yRellenar][xRellenar] == ' '):
			matriz[yRellenar][xRellenar] = caracterRelleno(xRellenar, yRellenar, posicionPuerta, orientacion) 
		
		if (orientacion == VERTICAL):
			yRellenar += 1
		else:
			xRellenar += 1

	#Llamada recursiva
	
	if (orientacion == VERTICAL):
		ponerPared(matriz, x, y, posicionInicial[0] - x, alto)
		ponerPared(matriz, posicionInicial[0] + 1, y, x + ancho - posicionInicial[0] - 1, alto)
	else:
		ponerPared(matriz, x, y, ancho, posicionInicial[1] - y)
		ponerPared(matriz, x, posicionInicial[1] + 1, ancho, y + alto - posicionInicial[1] - 1)
	

def main():

	try:
		parametros = obtenerParametros()
	except:
		print('Faltan parametros, la sintaxis correcta es: laberinto <anchoGrilla> <altoGrilla>.')
		return

	matriz = crearMatriz(parametros[0], parametros[1])
	ponerPared(matriz, 0, 0, parametros[0], parametros[1])

	imprimirLaberinto(matriz, parametros[0], parametros[1])


if __name__ == "__main__":
	main()
