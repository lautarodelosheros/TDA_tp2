import math

#Usando para el marco del laberinto los mismos simbolos que para las paredes
#hace que se vea mucho mejor. 
def determinar_simbolo_marco(fila):
	if(fila % 2 == 0):
		return '|'
	return '+'

def imprimir_laberinto(matriz, ancho, alto):

	archivo = open('mapa-laberinto.txt', 'w')

	archivo.write('+ ');
	archivo.write('+-' * int(math.ceil((ancho - 2)/ 2)))
	archivo.write('+\n')


	for i in range(alto):
		marco = determinar_simbolo_marco(i)

		#Determina si es puerta de entrada o marco del laberinto.
		archivo.write(marco)

		for j in range(ancho):
			archivo.write(matriz[i][j])

		#Determina si es puerta de salida o marco del laberinto.
		archivo.write(marco)

		archivo.write('\n')

	archivo.write('+-' * int(math.ceil((ancho - 2)/ 2)))
	archivo.write('+ +\n')
