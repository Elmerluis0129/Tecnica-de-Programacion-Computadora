"""
Escribir un programa que capture una lista de caracteres.
Indicaciones:
La longitud de la lista debe ser dinámica (capturada).
Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
Mostra la lista con los caracteres capturados y el total.
Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa7 ():
# Listas y variable a utilizar
    listaCaracteres = [] # Lista donde se guardan los caracteres. / PRINCIPAL.
    totalCaracteres =  len(listaCaracteres) # Para saber la longitud de la lista.


    print("""      
*-------------------------------*      
|Captura de caracteres en lista.|
*-------------------------------*
""") # Decorando el nombre del programa.

    while True:
        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
            maxCaracterLista = int(input("Ingrese la cantidad de caracter que va a introducir: ")) # Mandato para saber cuántos caracteres serán el límite (Longitud de la lista.)
            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue
    
    
    # Función while para que me iteré las veces necesarias.
    while len(listaCaracteres) != maxCaracterLista:
        caracter = input("Ingresa el caracter: ") # Mandato para guardar los caracteres en una variable.
        control = caracter.isdigit()
        if control:  
            print("\nLo sentimos, no se permiten dígitos. Por lo que el mismo no aparecerá en la lista.\nIntente de nuevo.\n") # Se le dice que no se permiten los dígitos.     
            continue
        
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
    
    print(em("""
*-----------------------------------------*
|  ¡Programa 7 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#