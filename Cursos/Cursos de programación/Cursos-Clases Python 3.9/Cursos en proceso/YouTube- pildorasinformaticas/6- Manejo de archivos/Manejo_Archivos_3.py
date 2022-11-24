from io import open

archivo_texto = open("Archivo.txt", "a") #Sirve para abrir el archivo o crearlo en el caso de no existir, la a indica que se agregara algo al arvhivo
archivo_texto.write("\nSiempre es una buena ocasión para estudiar Python") #Aqui agregamos esto al archivo
archivo_texto.close() #Aqui lo cerramos.