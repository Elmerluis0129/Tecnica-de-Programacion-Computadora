Algoritmo Ejercicio
	
	Definir x,c Como Entero
	Definir contadorV Como Entero
	Definir contador Como Entero
	Escribir 'Dame el primer valor'
	Leer x
	contadorV <- 1
	
	Mientras x<>0 Hacer
		
		c <- c+x
		contador <- contador+1
		contadorV <- contadorV+1
		Escribir 'Dame el valor #',contadorV
		Leer x
		
	FinMientras
	
	Escribir c,' ',contador
	
FinAlgoritmo
