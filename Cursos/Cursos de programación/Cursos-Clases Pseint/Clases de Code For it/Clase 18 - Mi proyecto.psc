Proceso TiendaRopa
	
	Definir PrecioPoloche, PrecioCamisa, PrecioJean, PrecioBlusa, PrecioTenis, PrecioReloj, PrecioPulsera, PrecioZapatos, PrecioBermudas Como Real;
	Definir CantTotal, CantPoloche, CantCamisa, CantJean, CantBlusa, CantTenis, CantReloj, CantPulsera, CantZapatos, CantBermudas Como Real;
	Definir Poloches, Camisas, Jeans, Tenis, Relojes, Pulseras, Zapatos, Bermudas Como Caracter;
	Definir Comprando Como Caracter;
	
	
	PrecioPoloche <- 70.99;
	PrecioCamisa <- 40.59;
	PrecioJean <- 50;
	PrecioBlusa <- 30.77;
	PrecioTenis <- 120.27;
	PrecioReloj <- 252;
	PrecioPulsera <- 100.50;
	PrecioZapatos <- 82.1;
	PrecioBermudas <- 31.5;
	
	
	Escribir "TIENDA DE ROPA VIRTUAL";
	Escribir "--------------------------------------------";
	Escribir "Tenemos:";
	Escribir "";
	Escribir "Poloches a ", PrecioPoloche, "$";
	Escribir "Camisas a ", PrecioCamisa, "$";
	Escribir "Jeans a ", PrecioJean, "$";
	Escribir "Blusas a ", PrecioBlusa, "$";
	Escribir "Tenis a ", PrecioTenis, "$";
	Escribir "Relojes a ", PrecioReloj, "$";
	Escribir "Pulseras a ", PrecioPulsera, "$";
	Escribir "Zapatos a ", PrecioZapatos, "$";
	Escribir "Bermudas a ", PrecioBermudas, "$";
	Escribir "";
	Escribir "--------------------------------------------";
	Escribir "";
	
	Escribir "Presiona Enter para continuar";
	Leer Comprando;
	Escribir "";
	
	Si Comprando = "" Entonces
		Escribir "�Qu� deseas comprar?";
		Leer Comprando;
		
		Si Comprando = "Poloches" Entonces
			Escribir "�Cu�ntos poloches deseas?";
			Leer CantPoloche;
			
			Si Comprando = "Camisas" Entonces
				Escribir "�Cu�ntas camisas deseas?";
				Leer CantCamisa;
				
				Si Comprando = "Jeans" Entonces
					Escribir "�Cu�ntos jeans deseas?";
					Leer CantJean;
					
					Si Comprando = "Blusas" Entonces
						Escribir "�Cu�ntas blusas deseas?";
						Leer CantBlusa;
						
						Si Comprando = "Tenis" Entonces
							Escribir "�Cu�ntos tenis deseas?";
							Leer CantTeni;
							
							Si Comprando = "Relojes" Entonces
								Escribir "Cu�ntos relojes deseas?";
								Leer CantReloj;
								
								Si Comprando = "Pulseras" Entonces
									Escribir "�Cu�ntas pulseras deseas?";
									Leer CantPulsera;
									
									Si Comprando = "Zapatos" Entonces
										Escribir "�Cu�ntos zapatos deseas?";
										Leer CantZapato;
										
										Si Comprando = "Bermudas" Entonces
											Escribir "�Cu�ntas bermudas deseas?";
											Leer CantBermuda;
											
										CantTotal <- CantBermuda * PrecioBermuda;
										Escribir "Precio a pagar: ",CantTotal, "$";
										FinSi
										
									CantTotal <- CantZapato * PrecioZapato;
									Escribir  "Precio a pagar: ",CantTotal, "$";
										
									FinSi
								CantTotal <- CantPulsera * PrecioPulsera;
								Escribir 	"Precio a pagar: ",CantTotal, "$";
									
								FinSi
							CantTotal <- CantReloj * PrecioReloj;
							Escribir 	"Precio a pagar: ",CantTotal, "$";
								
							FinSi
						CantTotal <- CantTeni * PrecioTeni;
						Escribir 	"Precio a pagar: ",CantTotal, "$";
							
						FinSi
					CantTotal <-	CantBlusa * PrecioBlusa;
					Escribir 	"Precio a pagar: ",CantTotal, "$";
						
					FinSi
				CantTotal <- CantJean * PrecioJean;
				Escribir 	"Precio a pagar: ",CantTotal, "$";
					
				FinSi
			CantTotal <- CantCamisa * PrecioCamisa;
			Escribir 	"Precio a pagar: ",CantTotal, "$";
				
			FinSi
		CantTotal <- CantPoloche * PrecioPoloche;	
		Escribir "Precio a pagar: ",CantTotal, "$";
			
		FinSi
		
		
		
	FinSi
	
FinProceso