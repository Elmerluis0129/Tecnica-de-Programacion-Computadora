from io import open

archivo_texto = open("archivo.txt", "r+") #Se abre en modo escritura y en modo lectura

print(archivo_texto.read()) #Sirve para leer el archivo

archivo_texto.seek(35) #Sirve para ubicar donde se estara el puntero, en este caso en la posicion 35

print("\n",archivo_texto.read()) #Sirve para leer el archivo

archivo_texto.close()