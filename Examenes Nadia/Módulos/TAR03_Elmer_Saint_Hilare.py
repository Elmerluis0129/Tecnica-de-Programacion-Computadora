""" 
Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh 
consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios. Calcule el precio a pagar de acuerdo 
con la siguiente tabla. (Tabla en la plataforma UNPHU)
Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.


def programa3 (): # Esta linea no es parte del ejercicio, es del examen.
    print("""\n
*------------------------------------------------------*
|Precio a pagar por el suministro de energía eléctrica.|
*------------------------------------------------------*
""")# Decorando el nombre.

    print("""
*--------------------------------------*
|Tipos de instalacciones a seleccionar.|
*--------------------------------------*
\n""")# Decorando la pregunta.

    print("""
*---------------*
|R = Residencial|
|---------------|
|C = Comercial  |
|---------------|
|I = Industrial |
*---------------*
\n""")# Decorando las opciones.

# Declaro las variables a utilizar, tipo de instalacion y kilo waths consumidos.
    TipoInstalacion = input("Ingrese el tipo de instalación: ") # Tipo de instalacion.
    
# Condiciones para saber que tipo de instalacion tienen los usuarios.
    while True: # NECESARIO PARA MI CONTROL DE DATA BASURA
        if TipoInstalacion == "R":# Aqui para saber si su instalacion es tipo R.
            while True: #DATA BASURA
                try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                    kwhConsumido = int(input("Ingrese la cantidad de Kilo Watts consumidos: "))# Kilo Whatts consumidos.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("Lo siento, no se permite data basura.\n Por favor intentarlo de nuevo.\n")
                    continue
            if kwhConsumido == 1 or kwhConsumido <= 500:# Sentencia para saber si la cantidad de Kilo watts es menor a 500.
                print("\nEl precio a pagar es de: RD$550.00")# Precio a pagar dependiendo de si su consumo es menor a 500.
            elif kwhConsumido > 500:# Sentencia para saber si la cantidad de Kilo watts es mayor a 500.
                print("\nEl precio a pagar es de: RD$850.00")# Precio a pagar dependiendo de si su consumo es mayor a 500.
            break
        elif TipoInstalacion == "C":# Aqui para saber si su instalacion es tipo C.
            while True: #DATA BASURA
                try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                    kwhConsumido = int(input("Ingrese la cantidad de Kilo Watts consumidos: "))# Kilo Whatts consumidos.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("Lo siento, no se permite data basura.\n Por favor intentarlo de nuevo.\n")
                    continue
            if kwhConsumido == 1 or kwhConsumido <= 1000:#Sentencia para saber si la cantidad de Kilo watts es menor a 1000.
                print("\nEl precio a pagar es de: RD$1,300.00")#Precio a pagar dependiendo de si su consumo es menor a 1000.
            elif kwhConsumido > 1000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 1000.
                print("\nEl precio a pagar es de: RD$2,500.00")#Precio a pagar dependiendo de si su consumo es mayor a 1000.
            break
        elif TipoInstalacion == "I":# Aqui para saber si su instalacion es tipo I.
            while True: #DATA BASURA
                try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                    kwhConsumido = int(input("Ingrese la cantidad de Kilo Watts consumidos: "))# Kilo Whatts consumidos.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("Lo siento, no se permite data basura.\n Por favor intentarlo de nuevo.\n")
                    continue
            if kwhConsumido == 1 or kwhConsumido <= 5000:# Sentencia para saber si la cantidad de Kilo watts es menor a 5000.
                print("\nEl precio a pagar es de: RD$3,800.00")# Precio a pagar dependiendo de si su consumo es menor a 5000.
            elif kwhConsumido > 5000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 5000.
                print("\nEl precio a pagar es de: RD$4,200.00")# Precio a pagar dependiendo de si su consumo es mayor a 5000.
            break
        else:
            while True: # DATA BASURA
                print("\nLo siento, lo que haz introducido no es la letra que corresponde a una de las opciones de tipo de instalacion. \n Por favor vuelve a intentarlo.\n") #En caso de que el usuario no marque correctamente la letra de su tipo de instalacion.
                TipoInstalacion = input("Ingrese el tipo de instalación: ") # Tipo de instalacion.
                if TipoInstalacion == "R" or TipoInstalacion == "I" or TipoInstalacion == "C":
                    break
            continue
            
        
#========================== Agradecimiento por usar el programa =========================#  

    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """

    print(em("""
*-----------------------------------------*
|  ¡Programa 3 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#