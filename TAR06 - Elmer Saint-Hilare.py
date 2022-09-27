# Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.
# El monto del préstamo debe ser solicitado.
# Se debe solicitar la cantidad mensual que se desea pagar.
# Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.
# Elmer Saint-Hilare 21-1354

print("Tiempo en meses para pagar su préstamo.\n")

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
    print("\nDatos registrados y guardados.\n")

mesesApagar = MontoPrestamo / CantidadMensual
operacion = CantidadMensual * mesesApagar

while operacion != MontoPrestamo:
    if mesesApagar == 1:
        print("Con los proporcionados, estará completando su préstamo en " +str(mesesApagar) + " mes.\n")
        
    elif mesesApagar > 1:
        print("Con los datos proporcionados, estará completando su préstamo en " +str(mesesApagar) + " meses.\n")
        
#TODO RECORDAR BUSCAR LA FORMA DE HACER QUE EL BUCLE DE MAS DE UNA VUELTA SI NO CUMPLE LA CONDICION, PARA QUE SE MANIFIESTE REALMENTE EL USO DE WHILE
        



