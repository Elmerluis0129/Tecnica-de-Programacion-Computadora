Proceso CalculadoraBasica
	
	Definir num1, num2 Como Real;
	Definir Resultado Como Real;
	
	Escribir "CALCULADORA B�SICA"; 
	
	
	Escribir "Dame el primer n�mero";
	Leer num1;
	Escribir "Dame el segundo n�mero";
	Leer num2;
	
	//SUMA
	Resultado <- (num1 + num2);
	Escribir "El resultado de tu suma es de: ", Resultado;
	
	//RESTA
	Resultado <- (num1 - num2);
	Escribir "El resultado de tu resta es de: ", Resultado;
	
	//MULTIPLICACI�N
	Resultado <- (num1 * num2);
	Escribir "El resultado de tu multiplicaci�n es de: ", Resultado;
	
	//DIVISI�N
	Resultado <- (num1 / num2);
	Escribir "El resultado de tu divisi�n es de: ", Resultado;
	
	//RESIDUO
	Resultado <- (num1 % num2);
	Escribir "El resultado de tu residuo es de: ", Resultado;
	
	Escribir "Pulsa cualquier tecla para salir...";
	
FinProceso