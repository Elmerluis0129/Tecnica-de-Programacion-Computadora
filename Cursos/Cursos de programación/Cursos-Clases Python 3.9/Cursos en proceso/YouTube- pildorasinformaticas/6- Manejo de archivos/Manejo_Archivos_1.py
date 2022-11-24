from io import open

archivo_texto = open("Archivo.txt", "w") #Sirve para abrir el archivo o crearlo en el caso de no existir, la w indica que se abrira tipo escritura

archivo_texto.write("Estupendo día para estudiar python \nel miércoles!!") #Sirve para escribir en el archivo, una vez abierto.
archivo_texto.close() #Sirve para cerrar el archivo.