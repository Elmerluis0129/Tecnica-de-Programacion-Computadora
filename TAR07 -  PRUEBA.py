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

MontoPrestamo = int(input("""
¿Cuál es el monto de su préstamo? 
> """))

CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))

mesesApagar = MontoPrestamo / CantidadMensual
AñosApagar = mesesApagar / 12
operacion = mesesApagar * CantidadMensual

while MontoPrestamo == CantidadMensual:
    print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n")
    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))

while True:
    if operacion == MontoPrestamo:
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")
        break
    else:
        print("¡Lo siento! la cantidad a pagar mensual no es muy exacta. Itente de nuevo.")
        CantidadMensual = int(input("¿Cuál es la cantidad mensual de su préstamo a pagar? > "))
        operacion = round(operacion)
#TODO RECUERDA AGREGAR LA DOCUMENTACION.
    
#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN