"""
Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.
Elmer Luis Saint-Hilare Rojo / 21-1354. 
"""
def programa2 ():
    import math #Aquí importo math para poder hacer uso de la raiz cuadrada.

    print("""
*--------------------------------------------------------*
|Cálculo de la raíz cuadrada de la suma de los cuadrados |
*--------------------------------------------------------*   
""")

    print("|------------------------------------|")
    numero1 = int(input(" Ingrese el primer número: "))#Aquí le pido al usuario el primer número.
    print("|------------------------------------|")
    numero2 = int(input(" Ingrese el segundo número: "))#Aquí le pido al usuario el segundo número.
    numero1cuadrado = numero1**2#Aquí elevo el primer número que me da el usuario al cuadrado.
    numero2cuadrado = numero2**2#Aquí elevo el segundo número que me da el usuario al cuadrado.
    operacion = (numero1cuadrado + numero2cuadrado)#Aquí es para que me sume los dos números ya elevados al cuadrado.

    #Salidas/proceso que el usuario verá.
    print("|----------------------------------------------|")
    print("\n El resultado de: ", str(numero1) + "^2 =", numero1cuadrado) #Aquí le muestra el mismo elevado al cuadrado.
    print("|----------------------------------------------|")
    print("\n El resultado de: ", str(numero2) + "^2 =", numero2cuadrado)#Aquí le muestra el mismo elevado al cuadrado.
    print("|----------------------------------------------|")
    print("\n La suma de los números es: ", numero1**2, "+", numero2**2, "=", operacion) #Aquí le muestra la suma de los números cuadrados.
    print("|----------------------------------------------|")
    print("\n La raiz de esa suma es: ", round(math.sqrt(operacion), 2))#Aquí le muestra ya el resultado de el problema resuelto y utilizamos math.sqrt para sacar la raiz.
    print("|----------------------------------------------|")

    #========================== Agradecimiento por usar el programa =========================#  

    """
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

    print("""
*----------------------------------------------------------------------------*
|  ¡Programa 2 Finalizado exitosamente! / By: Elmer Saint-Hilare 21-1354     |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#