Proceso InicioSesion
	
	Definir user, password, respuestaUser, respuestaPassword Como Caracter;
	
	user <- "Elmerluis2901";
	Password <- "password2021";
	
	Escribir "Bienvenido al sistema";
	Escribir "Ingresa tu usuario";
	Leer respuestaUser;
	Escribir "Ingresa tu contrase�a:";
	Leer respuestaPassword;
	
	Si user = respuestaUser y password = respuestaPassword Entonces
		Escribir "Has ingresado al sistema con �xito";
	SiNo
		Escribir "Lo sentimos, usuario o contrase�a incorrectos, vuelve a intentar m�s tarde";
	FinSi
	
	Escribir "Pulsa cualquier letra para salir...";
	
FinProceso
