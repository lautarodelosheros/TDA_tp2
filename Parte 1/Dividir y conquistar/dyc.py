from determinar_parametros import *
from core import *
from constantes import *
from imprimir import *


#Basado en la posiciona a escribir de la matriz se determina que simbolo usar para la pared o puerta. 
def caracter_relleno(x, y, posicion_puerta, orientacion):
	
	if(x == posicion_puerta[0] and y == posicion_puerta[1]):
		return ' '

	if(x % 2 != 0 and y % 2 != 0):
		return '+'

	if (orientacion == VERTICAL):
		return '|'
	else:
		return '-'

def poner_pared(matriz, x, y, ancho, alto):

	if (ancho < 2 or alto < 2):
		return;

	orientacion = determinar_orientacion_pared(ancho, alto)
	posicion_inicial = determinar_posicion_inicial_pared(x, y, ancho, alto, orientacion)
	posicion_puerta = determinar_posicion_puerta(posicion_inicial[0], posicion_inicial[1], ancho, alto, orientacion)	
	largo_pared = determinar_largo_pared(ancho, alto, orientacion)

	x_rellenar = posicion_inicial[0]
	y_rellenar = posicion_inicial[1]

	#Guardar pared en la matriz

	for i in range(largo_pared):
		if(matriz[y_rellenar][x_rellenar] == ' '):
			matriz[y_rellenar][x_rellenar] = caracter_relleno(x_rellenar, y_rellenar, posicion_puerta, orientacion) 
		
		if (orientacion == VERTICAL):
			y_rellenar += 1
		else:
			x_rellenar += 1

	#Llamada recursiva
	
	if (orientacion == VERTICAL):
		poner_pared(matriz, x, y, posicion_inicial[0] - x, alto)
		poner_pared(matriz, posicion_inicial[0] + 1, y, x + ancho - posicion_inicial[0] - 1, alto)
	else:
		poner_pared(matriz, x, y, ancho, posicion_inicial[1] - y)
		poner_pared(matriz, x, posicion_inicial[1] + 1, ancho, y + alto - posicion_inicial[1] - 1)
	
#Los parametros se ajustan al modelo de que las paredes son infinitesimales
#entonces el laberinto tiene tantas filas y columnas como las indicadas pero
#como no se pueden dibujar paredes infinitesimales se agregan filas y columnas
#para poder dibujarlas.

def crear_laberinto_dyc(ancho, alto):

	ancho_normalizado = 2 * ancho - 1
	alto_normalizado = 2 * alto - 1 

	matriz = crear_matriz(ancho_normalizado, alto_normalizado)
	poner_pared(matriz, 0, 0, ancho_normalizado, alto_normalizado)

	imprimir_laberinto(matriz, ancho_normalizado, alto_normalizado)


