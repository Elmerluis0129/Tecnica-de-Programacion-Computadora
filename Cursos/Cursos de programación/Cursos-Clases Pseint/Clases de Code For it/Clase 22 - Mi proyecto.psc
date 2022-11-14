Proceso Heladeria
	
	Definir CantVainilla,CantChocolate,CantFresa Como Real;
	Definir PrecioVaini,PrecioChoco,PrecioFre,DescuentoVainilla,DescuentoFresa,IVAvainilla,IVAchocolate,IVAfresa Como Real;
	Definir Respuesta Como Caracter;
	Definir CantTotal Como Real;
	Definir SaborHelado Como Caracter;
	Definir CantHelado Como Real;
	
	PrecioVaini <- 20.37;
	PrecioChoco <- 15.90;
	PrecioFre <- 18.20;
	DescuentoVainilla <- PrecioVaini*.20;
	DescuentoFresa <- PrecioFre*.20;
	IVAvainilla <- PrecioVaini*.10;
	IVAchocolate <- PrecioChoco*.10;
	IVAfresa <- PrecioFre*.10;
	
	Escribir 'HELADERIA EL DICHO';
	Escribir 'Buenas, tenemos tres tipos de helados:';
	Escribir ('---------------------------------------');
	Escribir 'Helados sin descuento';
	Escribir 'Helados de Chocolate ',PrecioChoco,'$';
	Escribir ('---------------------------------------');
	Escribir ('Helados con descuento de un 20%');
	Escribir 'Helados de Fresa ',PrecioFre,'$';
	Escribir 'Helados de Vainilla ',PrecioVaini,'$';
	Escribir ('---------------------------------------');
	Escribir '¿Cuántos helados deseas?';
	Leer CantHelado;
	Si CantHelado>1 Entonces
		Escribir '¿De qué sabor deseas tus ',CantHelado,' helados';
		Leer SaborHelado;
	SiNo
		Escribir '¿De qué sabor deseas tu helado';
		Leer SaborHelado;
	FinSi
	
	// HELADO CHOCOLATE
	
	Si SaborHelado='Chocolate' Entonces
		Escribir '¿Deseas ',CantHelado,' helados de chocolate? / Si o No';
		Leer Respuesta;
		Si Respuesta='Si' Entonces
			CantChocolate <- CantHelado;
			Escribir '¿Deseas comprar helados de otro sabor? / Si o No';
			Leer Respuesta;
			Si Respuesta='Si' Entonces
				Escribir '¿Deseas helado de vainilla? / Si o No';
				Leer Respuesta;
				Si Respuesta='Si' Entonces
					CantVainilla <- CantHelado;
					Escribir '¿Deseas comprar helado de fresa también? / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de fresa deseas?';
						Leer CantFresa;
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla)+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					FinSi
				SiNo
					Escribir '¿Deseas comprar helado de fresa / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de fresa deseas?';
						Leer CantFresa;
						CantTotal <- CantChocolate*PrecioChoco+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantChocolate*PrecioChoco;
						Escribir 'Su precio a pagar es de: ',CantTotal,'$';
					FinSi
				FinSi
			SiNo
				CantTotal <- CantChocolate*PrecioChoco;
				Escribir 'Su precio a pagar no tiene descuento, es de: ',CantTotal,'$';
			FinSi
		SiNo
			Escribir 'Error';
		FinSi
	FinSi
	
	// HELADO VAINILLA
	
	Si SaborHelado='Vainilla' Entonces
		Escribir '¿Deseas ',CantHelado,' helados de vainilla?';
		Leer Respuesta;
		Si Respuesta='Si' Entonces
			CantVainilla <- CantHelado;
			Escribir '¿Deseas comprar helados de otro sabor? / Si o No';
			Leer Respuesta;
			Si Respuesta='Si' Entonces
				Escribir '¿Deseas comprar helado de chocolate?';
				Leer Respuesta;
				Si Respuesta='Si' Entonces
					CantChocolate <- CantHelado;
					Escribir '¿Deseas comprar helado de fresa también? / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de fresa deseas?';
						Leer CantFresa;
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla)+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					FinSi
				SiNo
					Escribir '¿Deseas comprar helado de fresa / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de fresa deseas?';
						Leer CantFresa;
						CantTotal <- CantVainilla*PrecioVaini+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantVainilla*PrecioVaini-DescuentoVainilla;
						Escribir 'Su precio a pagar tiene un 20$ de descuento, son:',CantTotal,'$';
					FinSi
				FinSi
			SiNo
				CantTotal <- CantVainilla*PrecioVaini-DescuentoVainilla;
				Escribir 'Su precio a pagar tiene un 20$ de descuento, son: ',CantTotal,'$';
			FinSi
		SiNo
			Escribir 'Error';
		FinSi
	FinSi
	
	// HELADO FRESA
	
	Si SaborHelado='Fresa' Entonces
		Escribir '¿Deseas ',CantHelado,' helados de fresa?';
		Leer Respuesta;
		Si Respuesta='Si' Entonces
			CantFresa <- CantHelado;
			Escribir '¿Deseas comprar helados de otro sabor? / Si o No';
			Leer Respuesta;
			Si Respuesta='Si' Entonces
				Escribir '¿Deseas comprar helado de vainilla?';
				Leer Respuesta;
				Si Respuesta='Si' Entonces
					CantVainilla <- CantHelado;
					Escribir '¿Deseas comprar helado de chocolate también? / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de chocolate deseas?';
						Leer CantChocolate;
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla)+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantChocolate*PrecioChoco+((CantVainilla*PrecioVaini)-DescuentoVainilla);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					FinSi
				SiNo
					Escribir '¿Deseas comprar helado de chocolate? / Si o No';
					Leer Respuesta;
					Si Respuesta='Si' Entonces
						Escribir '¿Cuántos helados de chocolate deseas?';
						Leer CantChocolate;
						CantTotal <- CantChocolate*PrecioChoco+((CantFresa*PrecioFre)-DescuentoFresa);
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					SiNo
						CantTotal <- CantFresa*PrecioFre-DescuentoFresa;
						Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
					FinSi
				FinSi
			SiNo
				CantTotal <- CantFresa*PrecioFre-DescuentoFresa;
				Escribir 'Su precio a pagar tiene un 20% de descuento, son: ',CantTotal,'$';
			FinSi
		SiNo
			Escribir 'Error';
		FinSi
	FinSi
	Escribir '';
	Escribir 'Presione cualquier letra para salir...';
	
FinProceso
