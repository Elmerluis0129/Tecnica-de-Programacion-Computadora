Proceso BuscarMes
	
	Definir dias como entero;
	
	Escribir "Dame la cantidad de días que tiene el/los mes/es que buscas";
	Leer dias 
	
	segun dias hacer
		30: 
			Escribir "Los únicos meses que cuentan con 30 días son: Abril, Septiembre, Junio y Noviembre"
			
		31: 
			Escribir "Los únicos meses que cuentan con 31 días son: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre"
			
		De Otro Modo:
			Si dias = 28 Entonces
				Escribir "Febrero es el único mes que cuenta con ", dias, " días"
			SiNo
				Si dias = 29 Entonces
					Escribir "Febrero solo cuando el año es biciesto cuenta con ", dias, " días"
					
				FinSi
			FinSi
			
			Si dias < 28 Entonces
				Escribir "Lo siento, pero, ningún mes cuenta con: ", dias, " días"
			SiNo
				Si dias > 31 Entonces
					Escribir "Lo siento, pero, ningún mes cuenta con: ", dias, " días"
					
				FinSi
			FinSi
	FinSegun
	
FinProceso
