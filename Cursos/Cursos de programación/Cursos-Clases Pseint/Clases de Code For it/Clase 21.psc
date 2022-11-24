Proceso autoInteligente
	
	Definir colorSemaforo Como Caracter;
	
	Escribir "Escaneando el color del semáforo...";
	Escribir "Color detectado: (rojo, amarillo o verde)";
	Leer colorSemaforo;
	
	segun colorSemaforo hacer
		
		"verde": 
			Escribir "Avanazando el auto";
			
		"amarillo": 
			Escribir "Deteniendo el auto";
			
		"rojo":
			Escribir "Deteniendo el auto";
			
		De Otro Modo:
			Escribir "Error: Deteniendo el auto";
		
	FinSegun

	
FinProceso