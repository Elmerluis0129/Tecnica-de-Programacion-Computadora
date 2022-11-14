Proceso InicioSesion
	
	Definir user, password, respuestaUser, respuestaPassword Como Caracter;
	
	user <- "Elmerluis2901";
	Password <- "password2021";
	
	Escribir "Bienvenido al sistema";
	Escribir "Ingresa tu usuario";
	Leer respuestaUser;
	Escribir "Ingresa tu contraseña:";
	Leer respuestaPassword;
	
	Si user = respuestaUser y password = respuestaPassword Entonces
		Escribir "Has ingresado al sistema con éxito";
	SiNo
		Escribir "Lo sentimos, usuario o contraseña incorrectos, vuelve a intentar más tarde";
	FinSi
	
	Escribir "Pulsa cualquier letra para salir...";
	
FinProceso
