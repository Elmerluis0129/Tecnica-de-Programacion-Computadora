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

while MontoPrestamo == CantidadMensual:
    print("\nLo siento, no permitimos pagar el préstamo con un sólo pago, tiene que dividirlo mensualmente.\n")
    CantidadMensual = int(input("""
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))

mesesApagar = MontoPrestamo / CantidadMensual
AñosApagar = mesesApagar / 12
operacion = mesesApagar * CantidadMensual

while operacion == MontoPrestamo:
    if MontoPrestamo >= 1000000 and CantidadMensual < 83333.33:
        while CantidadMensual < 83333.33:
            CantidadMensual = int(input(""""
¡Lo siento! la cantidad a pagar mensual es muy baja, por lo que excede el límite de años(meses) establecidos por la empresa. 
Por favor ingrese una cantidad por encima de los 83,500 pesos.
        
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
    if MontoPrestamo >= 500000 and CantidadMensual < 2100:
        while CantidadMensual < 2100:
            CantidadMensual = int(input(""""
¡Lo siento! la cantidad a pagar mensual es muy baja, por lo que excede el límite de años(meses) establecidos por la empresa. 
Por favor ingrese una cantidad por encima de los 2,250 pesos.
        
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))

    if MontoPrestamo >= 100000 and CantidadMensual < 425:
        while CantidadMensual < 425:
            CantidadMensual = int(input(""""
¡Lo siento! la cantidad a pagar mensual es muy baja, por lo que excede el límite de años(meses) establecidos por la empresa. 
Por favor ingrese una cantidad por encima de los 450 pesos.
        
¿Cuál es la cantidad mensual de su préstamo a pagar? 
> """))
    else:
        print("\nCon los datos proporcionados, estará completando su préstamo en " ,round(mesesApagar, 2), " meses o \n", round(AñosApagar, 2), " años\n")
        break
    
#TODO RECUERDA AGREGAR LA DOCUMENTACION.
    
#Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")#Decorando el agradecimiento.
#FIN