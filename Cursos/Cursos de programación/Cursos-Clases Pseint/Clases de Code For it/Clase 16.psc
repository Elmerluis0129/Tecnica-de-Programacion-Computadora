Proceso ContinuacionEstructuraDS
	
	Definir calif Como Real;
	
	Escribir 'Ingresa tu calificaci�n final:';
	Leer calif;
	
	Si calif >= 6 y calif <= 10 Entonces
		Escribir 'Felicidades, est�s aprobado!';
	SiNo
		Escribir "Sentimos informarle que no ha aprobado...";
	FinSi
	
	Escribir "";
	Escribir "Pulse cualquier tecla para salir...";
	
FinProceso