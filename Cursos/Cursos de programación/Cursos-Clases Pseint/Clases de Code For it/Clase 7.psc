Proceso RestauranteAutomatico
	
	Definir CantHotdogs, CantPapas, CantBebidas Como Entero;
	Definir PrecioHotdogs, PrecioPapas, PrecioBebidas Como Real;
	Definir PrecioFinal Como Real;
	
	PrecioHotdogs <- 2.5;
	PrecioPapas <- .3;
	PrecioBebidas <- 1.59;
	
	Escribir "Restaurante El Hotdog";
	Escribir "�Cu�ntos Hotdogs desea comer?";
	Leer CantHotdogs;
	Escribir "�Cu�ntas Papas desea comer?";
	Leer CantPapas;
	Escribir "�Cu�ntas bebidas desea para tomar?";
	Leer CantBebidas;
	
	PrecioFinal <- (PrecioHotdogs * CantHotdogs) + (PrecioPapas * CantPapas) + (PrecioBebidas * CantBebidas);
	
	Escribir "Su total a pagar es de ", PrecioFinal, " dolares";
	Escribir "Gracias por preferirnos";
	
FinProceso