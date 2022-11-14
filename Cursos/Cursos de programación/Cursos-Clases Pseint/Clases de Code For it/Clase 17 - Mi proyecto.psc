Proceso mayorEdad
	
	Definir edad Como Entero;
	Definir nombre Como Caracter;
	
	Escribir "Ingresa tu nombre completo";
	Leer nombre;
	Escribir "Ingresa tu edad";
	Leer edad;
	
	
	Si edad >= 18  y edad <= 125 Entonces
		Escribir nombre, " tienes ",edad, " años, por lo tanto sí eres mayor de edad";
	FinSi
	
	Si edad < 18 Entonces
		Escribir nombre, " lo siento, pero no, no eres mayor de edad.";
	FinSi
	
	Si edad >= 126 Entonces
		Escribir nombre, " favor de poner una edad veraz";
	FinSi
	
	Escribir "";
	Escribir "Adiós, gracias por usar mi programa.";
	Escribir "";
	Escribir "Pulsa cualquier letra para salir...";
	
FinProceso