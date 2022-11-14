import pickle

#Con estas lineas codificamos la  lista de nombres a codigo binario
#lista_nombres = ["Pedro", "Ana", "Maria", "Isabel"]
#fichero_binario = open("lista_nombres", "wb") #Aqui creamos el archivo binario, con los permisos de escritura binaria "wb"

#pickle.dump(lista_nombres, fichero_binario) #Aqui hacemos un volcado de datos con nuestras variables
#fichero_binario.close()
#del fichero_binario #Con esto eliminamos el archivo de la memoria de la pc

#/---------------------------------------------------------------------------------------------------------------\#

#Con estas lineas leemos la lista de nombres que tenemos codificado con codigo binario
fichero = open("lista_nombres", "rb") #Aqui abrimos la lista de nombres con los permisos de lectura binaria "rb"
lista = pickle.load(fichero)
print(lista)