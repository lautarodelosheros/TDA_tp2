import random
import math
from constantes import *


#Utiliza un criterio euristico para determinar la orientacion de la pared.
#Es el mejor metodo encontrado por nosotros para tener mejor distribucion de paredes.
def determinar_orientacion_pared(ancho, alto):
	
	if(ancho > alto):
		return VERTICAL
	elif(alto > ancho):
		return HORIZONTAL
	else:
		return random.choice(lista_orientaciones)

#Determina la posicion mas cercana al centro de la habitacion que sea impar
def determinar_centro_impar(dimension):
	mitad = dimension / 2
	piso_mitad = int(math.floor(mitad))

	if (piso_mitad % 2 == 1):
		return piso_mitad
	elif (abs(piso_mitad + 1 - mitad) < abs(piso_mitad - 1 - mitad)):
		return piso_mitad + 1
	else:
		return piso_mitad - 1 
	

#La idea es que la pared este en el centro de la habitacion.
#Notas que x e y son siempre pares.
def determinar_posicion_inicial_pared(x, y, ancho, alto, orientacion):

	if (orientacion == VERTICAL):
		xPared = x + determinar_centro_impar(ancho)
		yPared = y
	else:
		xPared = x
		yPared = y + determinar_centro_impar(alto)

	return [xPared, yPared]


def determinar_posicion_puerta(posicion_inicial_x, posicion_inicial_y, ancho, alto, orientacion):

	if (orientacion == VERTICAL):
		posicion_x_puerta = posicion_inicial_x
		posicion_y_puerta = posicion_inicial_y + random.choice(range(0, alto - 1, 2))
	else:
		posicion_x_puerta = posicion_inicial_x + random.choice(range(0, ancho - 1, 2))
		posicion_y_puerta = posicion_inicial_y

	return [posicion_x_puerta, posicion_y_puerta]
	
def determinar_largo_pared(ancho, alto, orientacion):
	
	if (orientacion == VERTICAL):
		return alto
	else:
		return ancho

