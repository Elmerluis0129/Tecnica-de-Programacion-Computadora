Algoritmo areaPerimetrofiguras
	Definir opcionMenu Como Entero
	Definir lado,base,altura Como Real
	Escribir 'Calculadora de �rea y per�metro'
	Escribir 'Elige una figura para calcular su �rea y su per�metro'
	Escribir '1-Cuadro / 2- Rect�ngulo / 3-Tri�ngulo equilatero / 4-Salir '
	Leer opcionMenu
	Segun opcionMenu  Hacer
		1:
			// Procedimiento del cuadrado
			Escribir 'Ingresa la magnitud del lado'
			Leer lado
			Escribir 'Datos del cuadrado:'
			Escribir 'El �rea del cuadrado es de: ',lado*lado
			Escribir 'El per�metro del lado es de: ',lado*4
		2:
			// Procedimiento del rect�ngulo
			Escribir 'Ingresa la magnitud de la base:'
			Leer base
			Escribir 'Ingresa la magnitud de la altura:'
			Leer altura
			Escribir 'Datos del rect�ngulo: '
			Escribir 'El �rea del rect�ngulo es de:',base*altura
			Escribir 'El per�metro del rect�ngulo es: ',(base*2)+(altura*2)
		3:
			// Procedimiento del tri�ngulo equilatero
			Escribir 'Ingresa la magnitud de la base:'
			Leer base
			Escribir 'Ingresa la magnitud de la altura'
			Leer altura
			Escribir 'Datos del tri�ngulo equilatero:'
			Escribir 'El �rea del tri�ngulo equilatero es de:',(base*altura)/2
			Escribir 'El per�metro del tri�ngulo equilatero es de:',base*3
		4:
			Escribir "Hasta luego, ha salido del programa con �xito"
			
		De Otro Modo:
			Escribir "Lo siento, pero, el n�mero que ha elegido no est� entre la lista, favor e intente de nuevo!"
	FinSegun
	
	Escribir "El programa ha finalizado con �xito, gracias por utilizarlo."
	Escribir "PULSE CUALQUIER LETRA PARA SALIR..."
	
FinAlgoritmo
