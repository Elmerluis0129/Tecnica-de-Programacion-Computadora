Proceso ConvertorTemperaturas
	
	Definir cel, fah, kel Como Real;
	
	Escribir "CONVERSOR DE UNIDADES DE TEMPERATURA";
	Escribir "Escribe la temperatura en grados celsius";
	Leer cel;
	
	fah <- (cel*1.8)+32;
	Kel <- cel + 273.15;

	
	Escribir "----------------------------";
	Escribir "Celsius: ",cel,"°C";
	Escribir "Fahrenheit: ",fah,"°F";
	Escribir "Kelvin: ",kel, "°K";
	Escribir "----------------------------";
	
	Escribir "Presiona cualquier tecla para salir...";
	
FinProceso