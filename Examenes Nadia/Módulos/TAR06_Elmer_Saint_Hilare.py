"""
Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.\
Indicaciones: 
El monto del préstamo debe ser solicitado.
Se debe solicitar la cantidad mensual que se desea pagar.
Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.
Elmer Saint-Hilare 21-1354
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

def programa6 ():
    print("""
*---------------------------------------*
|Tiempo en meses para pagar su préstamo.|
*---------------------------------------*
""")#Decorando el nombre.

    while True: # DATA BASURA
        try:
            sistema = int(input("""
*----------------------------------------------------------------------------------*
|                         ¿Qué sistema desea seleccionar?                          |
|----------------------------------------------------------------------------------|
|1- Nuevo / Este no pagas impuestos pero tiene límite de tiempo para pagar         |
|2- Antiguo / Este pagas impuestos luego de exceder los 10 años a pagar el préstamo|
*----------------------------------------------------------------------------------*
> """)) #Sistemas, pagar impuestos o no.

            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue
    
# Condición para saber si el sistema que elige está fuera del menú.
    if sistema != 1 and sistema != 2:
        while True: # DATA BASURA
            while True: # DATA BASURA
                try:
                    sistema = int(input("""
*----------------------------------------------------------------------------------*
|                         ¿Qué sistema desea seleccionar?                          |
|----------------------------------------------------------------------------------|
|1- Nuevo / Este no pagas impuestos pero tiene límite de tiempo para pagar         |
|2- Antiguo / Este pagas impuestos luego de exceder los 10 años a pagar el préstamo|
*----------------------------------------------------------------------------------*
> """)) #Sistemas, pagar impuestos o no.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                    continue
            
            if sistema == 1 or sistema == 2:
                break
            else: continue
            
    if sistema == 2: # Sistema 2.
        while True: # DATA BASURA
                try:
                    MontoPrestamo = int(input("""
¿Cuál es el monto de su préstamo? 
> """)) # Mandato para saber la cantidad de su préstamo.
    
                    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))# Mandato para saber la cantidad de su mensualidad.
                    while MontoPrestamo == CantidadMensual: # While para saber si pone la misma cantidad a pagar.
                        print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n") # No está permitido hacer un sólo pago el préstamo
                        CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))# Mandato para saber la cantidad de su mensualidad.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                    continue

    elif sistema == 1:# Sistema 1.
        print("""\n
Límite de tiempo por cantidad de préstamo:
*-------------------------------------------------------------------*
|Préstamo mayor o igual a: RD$1,000,000 pesos. / 180 meses - 15 años|
|-------------------------------------------------------------------|
|Préstamo mayor o igual a: RD$500,000 pesos / 96 meses - 8 años     |
|-------------------------------------------------------------------|
|Préstamo mayor o igual a: RD$100,000 pesos / 48 meses - 4 años     |
|-------------------------------------------------------------------|
|Préstamo menor a: RD$100,000 pesos / 24 meses - 2 años             |
*-------------------------------------------------------------------*       
""") # Tabla con los límites por préstamos.
        while True: # DATA BASURA
                try:
                    MontoPrestamo = int(input("""
¿Cuál es el monto de su préstamo? 
> """)) # Mandato para saber la cantidad de su préstamo.
    
                    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))# Mandato para saber la cantidad de su mensualidad.
                    while MontoPrestamo == CantidadMensual: # While para saber si pone la misma cantidad a pagar.
                        print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n") # No está permitido hacer un sólo pago el préstamo
                        CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))# Mandato para saber la cantidad de su mensualidad.
                    break
                except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                    print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                    continue
    

#////////////////////////////////////////////////////////////////////////SISTEMA 1/////////////////////////////////////////////////////////////////////// 

# SISTEMA 1 Y 2. VARIABLES GENERALES
    mesesApagar = MontoPrestamo / CantidadMensual
    AñosApagar = mesesApagar / 12

    while sistema == 1: # Función para el sistema 1 (Nuevo).
        if MontoPrestamo >= 1000000 and mesesApagar < 180:  # Para saber si no excede el límite de meses-años en la cantidad de préstamo igual o mayor a 1M.
            print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n") # Calcular los meses si cumple.
            break # Acabar while.
        elif MontoPrestamo >= 1000000 and mesesApagar > 180: # Ejecutar esas sentencias de código hasta que se cumpla la primera condición de si excede límites o no.
            control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
            while True: # DATA BASURA
                    while mesesApagar > 180: # Límites para el préstamo de 100k.
                        if control == "si":
                            print("\nLo siento, pero, excede los límites de la empresa (15 años/180 meses) para esta cantidad de préstamo.\n Por favor, aumente su pago mensual.")
                        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
                            # Actualizamos valores de variables por cada cambio que hagan en cada iteración.
                            mesesApagar = MontoPrestamo / CantidadMensual
                            AñosApagar = mesesApagar / 12
                            # Condición para saber si ya puedo cerrar el while del límite de 180.
                            if mesesApagar < 180:
                                break
                            else: 
                                control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                                continue
                        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                            control = "no" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                            continue
                    mesesApagar = MontoPrestamo / CantidadMensual
                    AñosApagar = mesesApagar / 12
                    break
            
    #---------------------------------------------------------------------------------------------------------------------------------------------------------#
        if MontoPrestamo >= 500000 and mesesApagar < 96: 
            print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")   # Calcular los meses si cumple.  
            break # Acabar while
        elif MontoPrestamo >= 500000 and mesesApagar > 96: # Ejecutar esas sentencias de código hasta que se cumpla la primera condición de si excede límites o no.
            control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
            while True: # DATA BASURA
                    while mesesApagar > 96: # Límites para el préstamo de 100k.
                        if control == "si":
                            print("\nLo siento, pero, excede los límites de la empresa (8 años/96 meses) para esta cantidad de préstamo.\n Por favor, aumente su pago mensual.")
                        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
                            # Actualizamos valores de variables por cada cambio que hagan en cada iteración.
                            mesesApagar = MontoPrestamo / CantidadMensual
                            AñosApagar = mesesApagar / 12
                            # Condición para saber si ya puedo cerrar el while del límite de 96.
                            if mesesApagar < 96:
                                break
                            else: 
                                control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                                continue
                        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                            control = "no" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                            continue
                    mesesApagar = MontoPrestamo / CantidadMensual
                    AñosApagar = mesesApagar / 12
                    break
            
        #---------------------------------------------------------------------------------------------------------------------------------------------------------#
        elif MontoPrestamo >= 100000 and mesesApagar < 48: 
            print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")  # Calcular los meses si cumple.   
            break # Acabar while
        elif MontoPrestamo >= 100000 and mesesApagar > 48: # Ejecutar esas sentencias de código hasta que se cumpla la primera condición de si excede límites o no.
            control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
            while True: # DATA BASURA
                    while mesesApagar > 48: # Límites para el préstamo de 100k.
                        if control == "si":
                            print("\nLo siento, pero, excede los límites de la empresa (4 años/48 meses) para esta cantidad de préstamo.\n Por favor, aumente su pago mensual.")
                        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
                            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
                            # Actualizamos valores de variables por cada cambio que hagan en cada iteración.
                            mesesApagar = MontoPrestamo / CantidadMensual
                            AñosApagar = mesesApagar / 12
                            # Condición para saber si ya puedo cerrar el while del límite de 48.
                            if mesesApagar < 48:
                                break
                            else: 
                                control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                                continue
                        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                            control = "no" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                            continue
                    mesesApagar = MontoPrestamo / CantidadMensual
                    AñosApagar = mesesApagar / 12
                    break
            
        #---------------------------------------------------------------------------------------------------------------------------------------------------------#
        elif MontoPrestamo < 100000 and mesesApagar < 24: 
            print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")  # Calcular los meses si cumple.   
            break # Acabar while.
        elif MontoPrestamo < 100000 and mesesApagar > 24: # Ejecutar esas sentencias de código hasta que se cumpla la primera condición de si excede límites o no.
            while mesesApagar > 24: # Límites para el préstamo de menor a 100k.
                control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                while True: # DATA BASURA
                        while mesesApagar > 24: # Límites para el préstamo de 100k.
                            if control == "si": 
                                print("\nLo siento, pero, excede los límites de la empresa (2 años/24 meses) para esta cantidad de préstamo.\n Por favor, aumente su pago mensual.")
                            try:
                                CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
                                # Actualizamos valores de variables por cada cambio que hagan en cada iteración.
                                mesesApagar = MontoPrestamo / CantidadMensual
                                AñosApagar = mesesApagar / 12
                                # Condición para saber si ya puedo cerrar el while del límite de 24.
                                if mesesApagar < 24:
                                    break
                                else: 
                                    control = "si" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                                    continue
                            except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
                                print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
                                control = "no" # Control para saber cuál mensaje mostrar, dependiendo de lo que introduzca el usuario.
                                continue
                        mesesApagar = MontoPrestamo / CantidadMensual
                        AñosApagar = mesesApagar / 12
                        break           
        

#////////////////////////////////////////////////////////////////////////SISTEMA 2///////////////////////////////////////////////////////////////////////

# SISTEMA ANTIGUO (2) VARIABLES
    impuestoUnMillonOMas = 10000 * AñosApagar
    impuestosQuinientosMil = 5000 * AñosApagar
    impuestosCienMil = 1000 * AñosApagar
    impuestosBajoCienMil = 100 * AñosApagar
    
    while sistema == 2: # While sistema 2.
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n") # Calcular los meses si cumple.
        if MontoPrestamo >= 1000000 and mesesApagar > 120: # Para los que tienen un préstamo de 1M o más y exede los 10 años.
            print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$10,000.") # Impuestos para préstamos de 1M o más.
            print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestoUnMillonOMas, 2)), "pesos.") # Cálculamos la cantidad total de los impuestos.
            print("\nEl total serían: ", "RD$" + str(round(impuestoUnMillonOMas + MontoPrestamo, 2)), "pesos.","\n") # Total a pagar.
            
        #---------------------------------------------------------------------------------------------------------------#
        elif MontoPrestamo >= 500000 and mesesApagar > 120: # Para los que tienen un préstamo de 500k o más y exede los 10 años.
            print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$5,000.") # Impuestos para préstamos de 500k o más.
            print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosQuinientosMil, 2)), "pesos.") # Cálculamos la cantidad total de los impuestos.
            print("\nEl total serían: ", "RD$" + str(round(impuestosQuinientosMil + MontoPrestamo, 2)), "pesos.","\n") # Total a pagar.
        
        #---------------------------------------------------------------------------------------------------------------#
        elif MontoPrestamo >= 100000 and mesesApagar > 120: # Para los que tienen un préstamo de 100k o más y exede los 10 años.
            print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$1,000.") # Impuestos para préstamos de 100k o más.
            print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosCienMil, 2)), "pesos.") # Cálculamos la cantidad total de los impuestos.
            print("\nEl total serían: ", "RD$" + str(round(impuestosCienMil + MontoPrestamo, 2)), "pesos.","\n") # Total a pagar.
        
        #---------------------------------------------------------------------------------------------------------------#
        elif MontoPrestamo < 100000 and mesesApagar > 120: # Para los que tienen un préstamo de menos de 100k y exede los 10 años.
            print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$100.") # Impuestos para préstamos menores a 100k.
            print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosBajoCienMil, 2)), "pesos.") # Cálculamos la cantidad total de los impuestos.
            print("\nEl total serían: ", "RD$" + str(round(impuestosBajoCienMil + MontoPrestamo, 2)), "pesos.","\n") # Total a pagar.
        break # Acabar while.
        
    #========================== Agradecimiento por usar el programa =========================#  
    
    """
    Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
    """
    
    print(em("""
*-----------------------------------------*
|  ¡Programa 6 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#