Proceso PorcentajeDeAlumno
	
	Definir TotalAlumno, Porcentaje1, Porcentaje2, Porcentaje3, Porcentaje4, area1, area2, area3, area4 Como Real;
	
	Escribir "Escribe la cantidad de alumno que hay en el �rea 1";
	Leer area1;
	Escribir "Escribe la cantidad de alumnos que hay en el �rea 2";
	Leer area2;
	Escribir "Escribe la cantidad de alumnos que hay en el �rea 3";
	Leer area3;
	Escribir "Escribe la cantidad de alumnos que hay en el �rea 4";
	Leer area4;
	Escribir "";
	
	
	
	Escribir "----------------------------------";
	Escribir "";
	Escribir "ALUMNOS POR �REA";
	Escribir "�rea F�sico Matem�ticas e ingenier�a: ",area1;
	Escribir "�rea Ciencias de la salud: ",area2;
	Escribir "�rea Ciencias Sociales: ",area3;
	Escribir "�rea Humanidades y artes: ",area4;
	Escribir "";
	
	
	Escribir "----------------------------------";
	Escribir "";
	Escribir "Total de Alumnos";
	TotalAlumno <- area1 + area2 + area3 + area4;
	Escribir "Hay ", TotalAlumno, " alumnos en total.";
	Escribir "";
	Escribir "----------------------------------";
	Escribir "";
	
	
	Escribir "Porcentaje de alumno por �rea";
	Escribir "";
	
	Porcentaje1 <- (area1 * 100) / TotalAlumno;
	Escribir "F�sico Matem�ticas e ingenier�a: ",Porcentaje1,"%";
	
	Porcentaje2 <- (area2 * 100) / TotalAlumno;
	Escribir "Ciencias de la salud: ",Porcentaje2,"%";
	
	Porcentaje3 <- (area3 * 100) / TotalAlumno;
	Escribir "Ciencias Sociales ",Porcentaje3,"%";
	
	Porcentaje4 <- (area4 * 100) / TotalAlumno;
	Escribir "Humanidades y artes ",Porcentaje4,"%";
	Escribir "";
	
	Escribir "Presiona cualquier letra para salir...";
	
FinProceso
