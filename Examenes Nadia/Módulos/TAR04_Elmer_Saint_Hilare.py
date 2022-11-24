"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
Elmer Saint-Hilare 21/1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa4 (): # Esta linea no es parte del ejercicio, es del examen.
#Declaro mi variable a utilizar.
    Lista = []#Aquí se almacenan todos los elementos que el usuario más adelante va a proporcionar.

    print("""
*--------------------------------------------*
|Ingresar las 5 palabras para crear la lista.|
*--------------------------------------------*
\n""")#Decorando la intrucción.

#Bucle for para hacer las iteraciones necesarias para crear la lista, en este caso 5 veces.
    for numero in range(5):
        #Aquí para saber qué mandato le va a dar al usuario dependiendo de qué valor tenga x en dicho momento.
        if numero == 0: #Aquí para la primera iteración tendrá un valor de 1 la x, por lo que le pondrá el 1er mandato.
            palabra1 = input("Ingresar la primera palabra para la lista: ")
            while True: # DATA BASURA
                condicion1 = palabra1.isdigit() # Valor donde me dice si es digito o no.
                if condicion1: 
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra1 = input("Ingresar la primera palabra para la lista: ")
                    continue
                elif len(palabra1) >= 2:
                    Lista.append(palabra1) # Agrego la palabra a la lista en caso de no ser basura.
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra1 = input("Ingresar la primera palabra para la lista: ")
                    continue
                
        elif numero == 1: #Aquí para la segunda iteración tendrá un valor de 2 la x, por lo que le pondrá el 2do mandato.
            palabra2 = input("Ingresar la segunda palabra para la lista: ")
            while True: # DATA BASURA
                condicion2 = palabra2.isdigit() # Valor donde me dice si es digito o no.
                if condicion2:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra2 = input("Ingresar la segunda palabra para la lista: ")
                    continue
                elif len(palabra2) >= 2:
                    Lista.append(palabra2) # Agrego la palabra a la lista en caso de no ser basura.
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra2 = input("Ingresar la segunda palabra para la lista: ")
                    continue
                
        elif numero == 2: #Aquí para la tercera iteración tendrá un valor de 3 la x, por lo que le pondrá el 2do mandato.
            palabra3 = input("Ingresar la tercera palabra para la lista: ")
            while True: # DATA BASURA
                condicion3 = palabra3.isdigit() # Valor donde me dice si es digito o no.
                if condicion3:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra3 = input("Ingresar la tercera palabra para la lista: ")
                    continue
                elif len(palabra3) >= 2:
                    Lista.append(palabra3) # Agrego la palabra a la lista en caso de no ser basura.
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra3 = input("Ingresar la tercera palabra para la lista: ")
                    continue
                
        elif numero == 3: #Aquí para la cuarta iteración tendrá un valor de 4 la x, por lo que le pondrá el 2do mandato.
            palabra4 = input("Ingresar la cuarta palabra para la lista: ")
            while True: # DATA BASURA
                condicion4 = palabra4.isdigit() # Valor donde me dice si es digito o no.
                if condicion4:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra4 = input("Ingresar la cuarta palabra para la lista: ")
                    continue
                elif len(palabra4) >= 2:
                    Lista.append(palabra4) # Agrego la palabra a la lista en caso de no ser basura.
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra4 = input("Ingresar la cuarta palabra para la lista: ")
                    continue
                
        elif numero == 4: #Aquí para la quinta iteración tendrá un valor de 5 la x, por lo que le pondrá el 2do mandato.
            palabra5 = input("Ingresar la quinta palabra para la lista: ")
            while True: # DATA BASURA
                condicion5 = palabra5.isdigit() # Valor donde me dice si es digito o no.
                if condicion5:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra5 = input("Ingresar la quinta palabra para la lista: ")
                    continue
                elif len(palabra5) >= 2:
                    Lista.append(palabra5) # Agrego la palabra a la lista en caso de no ser basura.
                    break
                else:
                    print("\nLo siento, no se acepta data basura.\n")
                    palabra5 = input("Ingresar la quinta palabra para la lista: ")
                    continue
            break #Esto sirve para cuanddo vaya por la 5ta iteración y se cumpla la condición el bucle for se rompa, terminando por completo con las iteraciones.
        
    #Aquí creo las variables que me van a contener tanto la entrada por teclado del usuario, como las veces que aparece la palabra.
    print(Lista)
    buscarPalabra = input("\nEscriba la palabra que desea buscar: ") #Aqui para saber que palabra desea buscar en la lista.
    control = buscarPalabra.isdigit()
    if len(buscarPalabra) >= 2 and not control:
            VecesPalabraAparece = Lista.count(buscarPalabra) #Para saber si la palabra aparece o no y cuantas veces en caso de sí.
            
    elif len(buscarPalabra) <= 1:
        while True: # DATA BASURA
            print("\nLo siento, no se acepta data basura.\n Vuelve a intentarlo.\n")
            buscarPalabra = input("\nEscriba la palabra que desea buscar: ") #Aqui para saber que palabra desea buscar en la lista.
            control = buscarPalabra.isdigit()
            if len(buscarPalabra) >= 2 and not control: # Si cumple ser mayor a 2 letras, pero no son numeros, entonces sale, de lo contrario no.
                VecesPalabraAparece = Lista.count(buscarPalabra) #Para saber si la palabra aparece o no y cuantas veces en caso de sí.
                break
            else: continue
    elif control:
        while True: # DATA BASURA
            print("\nLo siento, no se acepta data basura.\nVuelve a intentarlo.\n")
            buscarPalabra = input("\nEscriba la palabra que desea buscar: ") #Aqui para saber que palabra desea buscar en la lista. 
            control = buscarPalabra.isdigit()       
            if control: continue # if control quiere decir que no va a salir del bucle si sigue ingresando numeros.
            else:
                VecesPalabraAparece = Lista.count(buscarPalabra) #Para saber si la palabra aparece o no y cuantas veces en caso de sí.
                break   
    
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