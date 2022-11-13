"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
Elmer Saint-Hilare 21/1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa4 (): # Esta linea no es parte del ejercicio, es del examen.
#Declaro mis variables a utilizar.
    Lista = []#Aquí se almacenan todos los elementos que el usuario más adelante va a proporcionar.
    iteración = 1 #Aquí es para poder cambiar el mandato en el bucle for.

    print("""
*--------------------------------------------*
|Ingresar las 5 palabras para crear la lista.|
*--------------------------------------------*
\n""")#Decorando la intrucción.

#Bucle for para hacer las iteraciones necesarias para crear la lista, en este caso 5 veces.
    for numero in range(5):
        #Aquí para saber qué mandato le va a dar al usuario dependiendo de qué valor tenga x en dicho momento.
        if iteración == 1: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            palabra1 = input("Ingresar la primera palabra para la lista: ")
            while True: # DATA BASURA
                condicion1 = palabra1.isdigit()
                if condicion1:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra1 = input("Ingresar la primera palabra para la lista: ")
                    continue
                elif len(palabra1) >= 2:
                    Lista.append(palabra1)
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra1 = input("Ingresar la primera palabra para la lista: ")
                    continue
        elif iteración == 2: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            palabra2 = input("Ingresar la segunda palabra para la lista: ")
            while True: # DATA BASURA
                condicion2 = palabra2.isdigit()
                if condicion2:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra2 = input("Ingresar la segunda palabra para la lista: ")
                    continue
                elif len(palabra2) >= 2:
                    Lista.append(palabra2)
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra2 = input("Ingresar la segunda palabra para la lista: ")
                    continue
        elif iteración == 3: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            palabra3 = input("Ingresar la tercera palabra para la lista: ")
            while True: # DATA BASURA
                condicion3 = palabra3.isdigit()
                if condicion3:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra3 = input("Ingresar la tercera palabra para la lista: ")
                    continue
                elif len(palabra3) >= 2:
                    Lista.append(palabra3)
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra3 = input("Ingresar la tercera palabra para la lista: ")
                    continue
        elif iteración == 4: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            palabra4 = input("Ingresar la cuarta palabra para la lista: ")
            while True: # DATA BASURA
                condicion4 = palabra4.isdigit()
                if condicion4:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra4 = input("Ingresar la cuarta palabra para la lista: ")
                    continue
                elif len(palabra4) >= 2:
                    Lista.append(palabra4)
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra4 = input("Ingresar la cuarta palabra para la lista: ")
                    continue
        elif iteración == 5: #Aquí para la quinta iteración tendrá un valor de 5 la x, por lo que le pondrá el 2do mandato.
            palabra5 = input("Ingresar la quinta palabra para la lista: ")
            while True: # DATA BASURA
                condicion5 = palabra5.isdigit()
                if condicion5:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra5 = input("Ingresar la quinta palabra para la lista: ")
                    continue
                elif len(palabra5) >= 2:
                    Lista.append(palabra5)
                    break
                else:
                    palabra5 = input("Ingresar la quinta palabra para la lista: ")
                    print("\nLo siento, no se acepta data basura.\n")
                    continue
            break #Esto sirve para cuanddo vaya por la 5ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        iteración += 1 #Este es la magia del bucle, aquí la variable x irá aumentando su valor de 1 en 1, por lo que es lo que ayuda a que cada condición se vaya cumpliendo según aumente el valor de x.
        
    #Aquí creo las variables que me van a contener tanto la entrada por teclado del usuario, como las veces que aparece la palabra.
    print(Lista)
    buscarPalabra = input("\nEscriba la palabra que desea buscar: ") #Aqui para saber que palabra desea buscar en la lista.
    VecesPalabraAparece = Lista.count(buscarPalabra) #Para saber si la palabra aparece o no y cuantas veces en caso de sí.
    
    #Aquí uso estas condiciones para saber qué cantidad de veces aparece la palabra, y poder varíar la respuesta, tipo: una vez o tantas veces. o no aparece.
    if VecesPalabraAparece > 1:
        print(f"\nLa palabra: '{buscarPalabra}' aparece {VecesPalabraAparece} veces en la lista.") #Aquí si aparece más de 1 vez, usará "Veces".
    elif VecesPalabraAparece == 1:
        print(f"\nLa palabra: '{buscarPalabra}' aparece {VecesPalabraAparece} vez en la lista.") #Aquí si aparece 1 sola vez, usará "Vez".
    elif not buscarPalabra in Lista:
        print(f"\nLa palabra: '{buscarPalabra}' no aparece en la lista que haz creado anteriormente.")  #Aquí si no aparece la palabra se lo especifica.
    
    # ========================== Agradecimiento por usar el programa ========================= #  
    
    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """
    
    print(em("""
*-----------------------------------------*
|  ¡Programa 4 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
# ========================== Fin Agradecimiento por usar el programa ========================= #