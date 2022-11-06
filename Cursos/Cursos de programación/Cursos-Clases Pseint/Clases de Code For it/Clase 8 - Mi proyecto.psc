Proceso CalculadoraBasica
	
	Definir num1, num2 Como Real;
	Definir Resultado Como Real;
	
	Escribir "CALCULADORA BÁSICA"; 
	
	
	Escribir "Dame el primer número";
	Leer num1;
	Escribir "Dame el segundo número";
	Leer num2;
	
	//SUMA
	Resultado <- (num1 + num2);
	Escribir "El resultado de tu suma es de: ", Resultado;
	
	//RESTA
	Resultado <- (num1 - num2);
	Escribir "El resultado de tu resta es de: ", Resultado;
	
	//MULTIPLICACIÓN
	Resultado <- (num1 * num2);
	Escribir "El resultado de tu multiplicación es de: ", Resultado;
	
	//DIVISIÓN
	Resultado <- (num1 / num2);
	Escribir "El resultado de tu división es de: ", Resultado;
	
	//RESIDUO
	Resultado <- (num1 % num2);
	Escribir "El resultado de tu residuo es de: ", Resultado;
	
	Escribir "Pulsa cualquier tecla para salir...";
	
FinProceso