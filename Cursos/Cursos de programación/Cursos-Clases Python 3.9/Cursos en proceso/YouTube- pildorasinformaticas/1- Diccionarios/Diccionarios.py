midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid", "Rep. Dom.":"Sto. Dom."}
midiccionario["Italia"]='Lisboa' #Agregar elementos al diccionario
print(midiccionario)

midiccionario["Italia"]="Roma" #Reemplazar valor a las claves de un diccionario
print(midiccionario)

del midiccionario["Reino Unido"] #Eliminar clave de un diccionario
print(midiccionario)

key = midiccionario.keys() #Pedir las claves de uno o mas diccionarios
print("Las claves del diccionario son: {}".format(key))

value = midiccionario.values() #Pedir los valores de uno o mas diccionarios
print("Los valores del diccionario son: {}".format(value))

len1 = len(midiccionario) #Pedir la longitud de uno o mas diccionarios
print("La longitud del diccionario es: {} valores.".format(len1))