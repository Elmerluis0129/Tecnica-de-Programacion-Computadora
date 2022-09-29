# Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.\
# Indicaciones: 
# El monto del préstamo debe ser solicitado.
# Se debe solicitar la cantidad mensual que se desea pagar.
# Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.
# Elmer Saint-Hilare 21-1354

print("""
*---------------------------------------*
|Tiempo en meses para pagar su préstamo.|
*---------------------------------------*
""")

sistema = int(input("""
*----------------------------------------------------------------------------------*
|                         ¿Qué sistema desea seleccionar?                          |
|----------------------------------------------------------------------------------|
|1- Nuevo / Este no pagas impuestos pero tiene límite de tiempo para pagar         |
|2- Antiguo / Este pagas impuestos luego de exceder los 10 años a pagar el préstamo|
*----------------------------------------------------------------------------------*
> """))

if sistema == 2:
    MontoPrestamo = int(input("""
¿Cuál es el monto de su préstamo? 
> """))
    
    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
    while MontoPrestamo == CantidadMensual:
        print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n")
        CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
elif sistema == 1:
    print("""
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
""")
    MontoPrestamo = int(input("""
¿Cuál es el monto de su préstamo? 
> """))
    
    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
    while MontoPrestamo == CantidadMensual:
        print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n")
        CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
else:
    print("\nLo siento, respuesta incorrecta, vuelve a intentarlo y selecciona 1 o 2.\n")

#////////////////////////////////////////////////////////////////////////SISTEMA 1/////////////////////////////////////////////////////////////////////// 

# SISTEMA 1 Y 2. VARIABLES GENERALES
mesesApagar = MontoPrestamo / CantidadMensual
AñosApagar = mesesApagar / 12

while sistema == 1:
    if MontoPrestamo >= 1000000 and mesesApagar < 180: 
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")     
        break
    elif MontoPrestamo >= 1000000 and mesesApagar > 180:
        while mesesApagar > 180:
            print("\nLo siento, pero, excede los límites de la empresa (15 años) para esta cantidad de préstamo.")
            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
            mesesApagar = MontoPrestamo / CantidadMensual
            AñosApagar = mesesApagar / 12
            
    #---------------------------------------------------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo >= 500000 and mesesApagar < 96: 
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")     
        break
    elif MontoPrestamo >= 500000 and mesesApagar > 96:
        while mesesApagar > 96:
            print("\nLo siento, pero, excede los límites de la empresa (8 años) para esta cantidad de préstamo.")
            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
            mesesApagar = MontoPrestamo / CantidadMensual
            AñosApagar = mesesApagar / 12
            
    #---------------------------------------------------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo >= 100000 and mesesApagar < 48: 
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")     
        break
    elif MontoPrestamo >= 100000 and mesesApagar > 48:
        while mesesApagar > 48:
            print("\nLo siento, pero, excede los límites de la empresa (4 años) para esta cantidad de préstamo.")
            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
            mesesApagar = MontoPrestamo / CantidadMensual
            AñosApagar = mesesApagar / 12 
            
    #---------------------------------------------------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo < 100000 and mesesApagar < 24: 
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")     
        break
    elif MontoPrestamo < 100000 and mesesApagar > 24:
        while mesesApagar > 24:
            print("\nLo siento, pero, excede los límites de la empresa (2 años) para esta cantidad de préstamo.")
            CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
            mesesApagar = MontoPrestamo / CantidadMensual
            AñosApagar = mesesApagar / 12             
        

#////////////////////////////////////////////////////////////////////////SISTEMA 2///////////////////////////////////////////////////////////////////////

# SISTEMA ANTIGUO (2) VARIABLES
impuestoUnMillonOMas = 1000 * AñosApagar
impuestosQuinientosMil = 500 * AñosApagar
impuestosCienMil = 100 * AñosApagar
impuestosBajoCienMil = 10 * AñosApagar

while sistema == 2:
    print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")
    if MontoPrestamo >= 1000000 and mesesApagar > 120:
        print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$1000.")
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestoUnMillonOMas, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestoUnMillonOMas + MontoPrestamo, 2)), "pesos.","\n")
        
    #---------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo >= 500000 and mesesApagar > 120:
        print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$500.")
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosQuinientosMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosQuinientosMil + MontoPrestamo, 2)), "pesos.","\n")
    
    #---------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo >= 100000 and mesesApagar > 120:
        print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$100.")
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosCienMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosCienMil + MontoPrestamo, 2)), "pesos.","\n")
    
    #---------------------------------------------------------------------------------------------------------------#
    elif MontoPrestamo < 100000 and mesesApagar > 120:
        print("\nEl impuesto a pagar por años por arriba del límite(10 años) es de: RD$10.")
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosBajoCienMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosBajoCienMil + MontoPrestamo, 2)), "pesos.","\n")
    break
    
#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN