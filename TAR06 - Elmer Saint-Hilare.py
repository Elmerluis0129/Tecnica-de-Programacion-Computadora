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

modo = int(input("""
*----------------------------------------------------------------------------------*
|                         ¿Qué sistema desea seleccionar?                          |
|----------------------------------------------------------------------------------|
|1- Nuevo / Este no pagas impuestos pero tiene límite de tiempo para pagar         |
|2- Antiguo / Este pagas impuestos luego de exceder los 10 años a pagar el préstamo|
*----------------------------------------------------------------------------------*
> """))

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

mesesApagar = MontoPrestamo / CantidadMensual
AñosApagar = mesesApagar / 12
operacion = mesesApagar * CantidadMensual

# MODO ANTIGUO VARIABLES
impuestoUnMillonOMas = 1000 * AñosApagar
impuestosQuinientosMil = 500 * AñosApagar
impuestosCienMil = 100 * AñosApagar
impuestosBajoCienMil = 10 * AñosApagar

       
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
if modo == 2:
    while round(operacion) == MontoPrestamo:
        if MontoPrestamo >= 1000000:
            print("El impuesto a pagar por años es de: RD$1000.")
                
        elif MontoPrestamo >= 500000:
            print("El impuesto a pagar por años es de: RD$500.")

        elif MontoPrestamo >= 100000:
            print("El impuesto a pagar por años es de: RD$100.")
    
        break
    
    print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")
    if MontoPrestamo >= 1000000:
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestoUnMillonOMas, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestoUnMillonOMas + MontoPrestamo, 2)), "pesos.","\n")
    elif MontoPrestamo >= 500000:
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosQuinientosMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosQuinientosMil + MontoPrestamo, 2)), "pesos.","\n")
    elif MontoPrestamo >= 100000:
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosCienMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosCienMil + MontoPrestamo, 2)), "pesos.","\n")
    elif MontoPrestamo < 100000:
        print("Por lo que el impuesto serían: ", "RD$" + str(round(impuestosBajoCienMil, 2)), "pesos.")
        print("\nEl total serían: ", "RD$" + str(round(impuestosBajoCienMil + MontoPrestamo, 2)), "pesos.","\n")
    
#TODO RECUERDA AGREGAR LA DOCUMENTACION Y USAR WHILE EN EL MODO 1 QUE FALTA TAMBIEN.
    
#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN