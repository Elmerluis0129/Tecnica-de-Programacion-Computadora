Algoritmo Ejercicio2
	
	Definir x,c Como Entero
	
	Escribir 'Dame el primer valor'
	Leer x
	
	Mientras x >= 0 Hacer
		
		Si x >= 10 Y x<100 Entonces
			c <- c+x
			Escribir 'Dame el siguiente valor'
			Leer x
		SiNo
			Escribir "Dame el siguiente valor"
			Leer x
		FinSi
		
	FinMientras
	
	Escribir ""
	Escribir c
	Escribir ""
	Escribir "PRESIONA CUALQUIER LETRA PARA SALIR..."
	
FinAlgoritmo
