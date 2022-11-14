Proceso AyPtrapecio
	
	Definir lado, altura, baseMayor, baseMenor, area, perimetro Como Real;
	
	Escribir "CALCULADORA DE ÁREA Y PERÍMETRO DE UN TRAPECIO";
	Escribir "Ingresa la medida del lado del trapecio:";
	Leer lado;
	Escribir "Ingresa la altura del trapecio:";
	Leer altura;
	Escribir "Ingreasa la medida de la base mayor del trapecio:";
	Leer baseMayor;
	Escribir "Ingresa la medida de la base menor del trapecio:";
	Leer baseMenor;
	
	area <- ((baseMayor + baseMenor) * altura) / 2;
	perimetro <- baseMayor + baseMenor + (lado * 2);
	
	Escribir "Dibujo";
	Escribir "";
	
	Escribir "           ",baseMenor, "cm";
	Escribir "       -----------      ";
	Escribir "      / |",altura,"cm","     \ ",lado,"cm";
	Escribir "     /  |          \   ";
	Escribir "     ---------------    ";
	Escribir "           ",baseMenor,"cm";
	Escribir "";
	
	Escribir "===============================";
	Escribir "Área: ", area,"cm2";
	Escribir "Perímetro; ", perimetro,"cm";
	
	Escribir "Para terminar con el programa, presione cualquier letra";
	
	
	
FinProceso
