#ADICIÓN
print("*ADICIÓN")

mensaje = "Hola"
mensaje += " "
mensaje += "Elmer"
print(mensaje)
print("-----------------------------------------------")

#CONCATENACIÓN
print("*CONCATENACIÓN")

mensaje = "Hola"
espacio = " "
nombre = "Elmer"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado) # Para concatenar con el signo (+) se necesita pasar el resultado a strings, con str
print("-----------------------------------------------")

#BÚSQUEDA
print("*LA BÚSQUEDA")

#Buscar
print("-Buscando")
mensaje = "Hola Elmer"
buscar_subcadena = mensaje.find("Elmer")
print("La cadena: (Elmer) se encuentra en el espacio número: ", buscar_subcadena)
print()

#Extraer
print("-Extrayendo")
mensaje = "Hola Elmer, soy tu asistente personal, ¿en qué puedo ayudarte? Sr."
extraer_subcadena = mensaje[0:]
print(extraer_subcadena)
print("-----------------------------------------------")

#COMPARACIÓN
print("*COMPARACIÓN")
mensaje_uno = "Hola Elmer Luis"
mensaje_dos = "Hola Elmer Luis"
comparacion = mensaje_uno == mensaje_dos
print(mensaje_uno, " = ", mensaje_dos,"?", comparacion)



