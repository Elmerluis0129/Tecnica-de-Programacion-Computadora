Proceso BuscarMes
	
	Definir dias como entero;
	
	Escribir "Dame la cantidad de d�as que tiene el/los mes/es que buscas";
	Leer dias 
	
	segun dias hacer
		30: 
			Escribir "Los �nicos meses que cuentan con 30 d�as son: Abril, Septiembre, Junio y Noviembre"
			
		31: 
			Escribir "Los �nicos meses que cuentan con 31 d�as son: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre"
			
		De Otro Modo:
			Si dias = 28 Entonces
				Escribir "Febrero es el �nico mes que cuenta con ", dias, " d�as"
			SiNo
				Si dias = 29 Entonces
					Escribir "Febrero solo cuando el a�o es biciesto cuenta con ", dias, " d�as"
					
				FinSi
			FinSi
			
			Si dias < 28 Entonces
				Escribir "Lo siento, pero, ning�n mes cuenta con: ", dias, " d�as"
			SiNo
				Si dias > 31 Entonces
					Escribir "Lo siento, pero, ning�n mes cuenta con: ", dias, " d�as"
					
				FinSi
			FinSi
	FinSegun
	
FinProceso
