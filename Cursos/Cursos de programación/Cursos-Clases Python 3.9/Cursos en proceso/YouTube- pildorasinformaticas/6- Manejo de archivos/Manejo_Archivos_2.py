from io import open

archivo_texto = open("Archivo.txt", "r") #Sirve para abrir el archivo o crearlo en el caso de no existir, la r indica que se abrira tipo lectura
#texto = archivo_texto.read() #Sirve para leer lo que hay dentro del archivo y lo almacene en la variable

lineas_texto = archivo_texto.readlines()
archivo_texto.close() #Sirve para cerrar el archivo abierto en un esapacio en memoria de nuestra pc

#print("El archivo contiene esto: "+ texto)
print("El archivo contiene esto: ", lineas_texto)

