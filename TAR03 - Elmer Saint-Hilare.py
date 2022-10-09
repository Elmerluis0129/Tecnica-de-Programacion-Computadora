""" Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh 
consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios. Calcule el precio a pagar de acuerdo 
con la siguiente tabla. (Tabla en la plataforma UNPHU)"""
# Elmer Saint-Hilare 21-1354

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
TipoInstalacion = str(input("Ingrese el tipo de instalación: ")) # Tipo de instalacion.
kwhConsumido = int(input("Ingrese la cantidad de Kilo Watts consumidos: "))# Kilo Whatts consumidos.

# Condiciones para saber que tipo de instalacion tienen los usuarios.
if TipoInstalacion == "R":# Aqui para saber si su instalacion es tipo R.
    if kwhConsumido == 1 or kwhConsumido <= 500:# Sentencia para saber si la cantidad de Kilo watts es menor a 500.
        print("\nEl precio a pagar es de: RD$550.00")# Precio a pagar dependiendo de si su consumo es menor a 500.
    elif kwhConsumido > 500:# Sentencia para saber si la cantidad de Kilo watts es mayor a 500.
        print("\nEl precio a pagar es de: RD$850.00")# Precio a pagar dependiendo de si su consumo es mayor a 500.
elif TipoInstalacion == "C":# Aqui para saber si su instalacion es tipo C.
    if kwhConsumido == 1 or kwhConsumido <= 1000:#Sentencia para saber si la cantidad de Kilo watts es menor a 1000.
        print("\nEl precio a pagar es de: RD$1300.00")#Precio a pagar dependiendo de si su consumo es menor a 1000.
    elif kwhConsumido > 1000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 1000.
        print("\nEl precio a pagar es de: RD$2500.00")#Precio a pagar dependiendo de si su consumo es mayor a 1000.
elif TipoInstalacion == "I":# Aqui para saber si su instalacion es tipo I.
    if kwhConsumido == 1 or kwhConsumido <= 5000:# Sentencia para saber si la cantidad de Kilo watts es menor a 5000.
        print("\nEl precio a pagar es de: RD$3800.00")# Precio a pagar dependiendo de si su consumo es menor a 5000.
    elif kwhConsumido > 5000:# Sentencia para saber si la cantidad de Kilo watts es mayor a 5000.
        print("\nEl precio a pagar es de: RD$4200.00")# Precio a pagar dependiendo de si su consumo es mayor a 5000.
else:
    print("\nLo siento, lo que haz introducido no es la letra que corresponde a una de las opciones de tipo de instalacion. ") #En caso de que el usuario no marque correctamente la letra de su tipo de instalacion.
        
# Agradecimiento por usar el programa.
print("""
*----------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! / By: Elmer Saint-Hilare 21-1354 |
*----------------------------------------------------------------------------*
""")# Decorando el agradecimiento.
# FIN