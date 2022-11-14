Proceso TiendaRopa
	
	Definir CostoTotal, desc Como Real;
	
	
	Escribir "//TIENDA DE ROPA NEWSKIN//";
	Escribir "Ingresa el costo total a pagar";
	Leer CostoTotal;
	Escribir "";
	
	Escribir "-----------------Ticket-------------------";
	Escribir "Subtotal: $", CostoTotal;
	
	
	Si CostoTotal >= 2000 Entonces
		desc <- CostoTotal* 0.015;
		CostoTotal <- CostoTotal - desc;
		Escribir "Descuento de: $", desc;
		
	FinSi
	
	Escribir "Total: $", CostoTotal;
	Escribir "";
	Escribir "PULSE CUALQUIER TECLA PARA SALIR";
	
FinProceso