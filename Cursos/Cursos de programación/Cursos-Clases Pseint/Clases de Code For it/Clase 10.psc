Proceso ContinuacionDiagramaDeFlujos
	
	Definir base Como Real;
	Definir altura Como Real;
	Definir resultado1,resultado2 Como Real;
	
	Escribir 'Escribe la base del rectangulo';
	Leer base;
	Escribir 'Escribe la altura del rectangulo';
	Leer altura;
	
	resultado1 <- base*altura;
	resultado2 <- 2*(base+altura);
	
	Escribir "---------------------------------------------";
	Escribir 'El área del rectangulo es: ',resultado1;
	Escribir 'El perímetro del rectangulo es: ',resultado2;
	Escribir "---------------------------------------------";
	
	Escribir "Presione cualquier letra, para salir del programa.";
	
FinProceso