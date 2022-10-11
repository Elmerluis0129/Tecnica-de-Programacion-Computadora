# Escribir un programa que capture una lista de caracteres.
# Indicaciones:
# La longitud de la lista debe ser dinámica (capturada).
# Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
# Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
# Mostra la lista con los caracteres capturados y el total.
# Elmer Saint-Hilare 21-1354

# Listas y variable a utilizar
listaCaracteres = [] # Lista donde se guardan los caracteres. / PRINCIPAL.
listaVacia = [] # Lista secundaria (No tiene ni mucha importancia, ni mucha utilización sirve para identificar cuando sea 1 caracter o caracteres en una condición más adelante.) / SECUNDARIA.
totalCaracteres =  len(listaCaracteres) # Para saber la longitud de la lista.


print("""      
*-------------------------------*      
|Captura de caracteres en lista.|
*-------------------------------*
""") # Decorando el nombre del programa.

maxCaracterLista = int(input("Ingrese la cantidad de caracter que va a introducir: ")) # Mandato para saber cuántos caracteres serán el límite (Longitud de la lista.)

# Función while para que me iteré las veces necesarias.
while len(listaCaracteres) != maxCaracterLista:
    caracter = input("Ingresa el caracter: ") # Mandato para guardar los caracteres en una variable.
    if caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9": # Me sirve esta condición para saber si el usuario ingresa un dígito.
        print("\nLo sentimos, no se permiten dígitos.") # Se le dice que no se permiten los dígitos.
        if listaCaracteres == listaVacia: # Aquí uso la otra lista de arriba para especificar que si la lista principal se parece a la secundaria, entonces es porque la principal está vacía.
            print("\nAl parecer lo primero que introdujiste fue un dígito, por lo que la lista se encuentra vacía.", listaCaracteres, "\n") # Y Aquí le pongo un mandato únicamente para cuando la lista principal sea igual a la secundaria (Está VACÍA).     
        # Aquí es si se llegaron a capturar caracteres antes de que se interrumpiese el programa. Entonces los muestra.
        else:
            print("\nLa lista de caracteres capturados es: ", listaCaracteres, "\n")
            if totalCaracteres == 1: # Aquí la condición para poner un sólo mandato cuando sea singular. Oséa que tenga sólo un caracter.
                print("Con el total de: ", totalCaracteres, "caracter.\n")
            else:# Aquí la condición para poner un sólo mandato cuando sea plural. Oséa que tenga más de un caracter.
                print("Con el total de: ", totalCaracteres, "caracteres.\n")     
        break # Romper el while, cómo especifica el mandato cuando se ingrese un dígito.
    
    elif len(caracter) > 1: # Para omitir palabras, ósea aquellas que no cumplan con la condición del caracter, que sea 1, si es más de 1 ya no es un caractér.
        continue
    
    else: # Aquí para que no me agregue a la lista los números, sólo me agregue los caractéres.
        listaCaracteres.append(caracter) # Agregamos lo que tenga la variable caracter cuando llegue a esta línea de código.
        totalCaracteres =  len(listaCaracteres) # Especificamos que cada vez que me agregue un valor a la lista, que me le sume ese valor al total.
        
# Aquí es para cuándo el programa se ejecute todo bien y no haya ningún incombeniente, ya que no se ingresó un dígito.
if len(listaCaracteres) == maxCaracterLista:
    print("\nLa lista de caracteres capturados es: ", listaCaracteres, "\n")
    if totalCaracteres == 1: # Aquí la condición para poner un sólo mandato cuando sea singular. Oséa que tenga sólo un caracter.
        print("Con el total de: ", totalCaracteres, "caracter.\n")
    else: # Aquí la condición para poner un sólo mandato cuando sea plural. Oséa que tenga más de un caracter.
        print("Con el total de: ", totalCaracteres, "caracteres.\n") 

#========================== Agradecimiento por usar el programa =========================#  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#