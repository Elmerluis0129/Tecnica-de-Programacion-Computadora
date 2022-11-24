Algoritmo areaPerimetrofiguras
	Definir opcionMenu Como Entero
	Definir lado,base,altura Como Real
	Escribir 'Calculadora de área y perímetro'
	Escribir 'Elige una figura para calcular su área y su perímetro'
	Escribir '1-Cuadro / 2- Rectángulo / 3-Triángulo equilatero / 4-Salir '
	Leer opcionMenu
	Segun opcionMenu  Hacer
		1:
			// Procedimiento del cuadrado
			Escribir 'Ingresa la magnitud del lado'
			Leer lado
			Escribir 'Datos del cuadrado:'
			Escribir 'El área del cuadrado es de: ',lado*lado
			Escribir 'El perímetro del lado es de: ',lado*4
		2:
			// Procedimiento del rectángulo
			Escribir 'Ingresa la magnitud de la base:'
			Leer base
			Escribir 'Ingresa la magnitud de la altura:'
			Leer altura
			Escribir 'Datos del rectángulo: '
			Escribir 'El área del rectángulo es de:',base*altura
			Escribir 'El perímetro del rectángulo es: ',(base*2)+(altura*2)
		3:
			// Procedimiento del triángulo equilatero
			Escribir 'Ingresa la magnitud de la base:'
			Leer base
			Escribir 'Ingresa la magnitud de la altura'
			Leer altura
			Escribir 'Datos del triángulo equilatero:'
			Escribir 'El área del triángulo equilatero es de:',(base*altura)/2
			Escribir 'El perímetro del triángulo equilatero es de:',base*3
		4:
			Escribir "Hasta luego, ha salido del programa con éxito"
			
		De Otro Modo:
			Escribir "Lo siento, pero, el número que ha elegido no está entre la lista, favor e intente de nuevo!"
	FinSegun
	
	Escribir "El programa ha finalizado con éxito, gracias por utilizarlo."
	Escribir "PULSE CUALQUIER LETRA PARA SALIR..."
	
FinAlgoritmo
