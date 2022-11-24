"""
Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.
Elmer Luis Saint-Hilare Rojo / 21-1354. 
"""
from emoji import emojize as em # Esto no es parte del ejercicio, es decoración.

# ==== Importando time ==== #
"""
Aquí lo importo para usar la función sleep y poder controlar la velocidad de iteración del bucle for.
"""
import time
# ==== Fin Importando time ==== #

# ================ Barra de porcentaje ================ #
"""
Aquí declaro mi limite una función, que es la que se encarga de hacer los cálculos de la barra.
Con el for es para darle formato a la barra de carga, de tal manera que vaya haciendolo con un tiempo de 0,7 por iteración.
"""
limite = 50

def barraProgreso(segmento, total, longitud):
    porcentaje = segmento / total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{'+' * completado}{'-' * restante}{porcentaje:.2%}]"
    return barra

input("\nPresione Enter para iniciar el programa... \n")
print("\nCargando... Por favor espere.")
for i in range(limite+1):
    time.sleep(0.03)
    print(barraProgreso(i, limite, 50), end = "\r")
    
print("\n")
    
# ============== Fin Barra de porcentaje ============== #


def programa2 (): # Esta linea no es parte del ejercicio, es del examen.
    import math #Aquí importo math para poder hacer uso de la raiz cuadrada.

    print("""
*--------------------------------------------------------*
|Cálculo de la raíz cuadrada de la suma de los cuadrados |
*--------------------------------------------------------*   
""")
    while True:
        try: # Aquí le digo al programa que intente las líneas de códigos que están dentro de la misma.
            print("|------------------------------------|")
            numero1 = int(input(" Ingrese el primer número: "))#Aquí le pido al usuario el primer número.
            print("|------------------------------------|")
            numero2 = int(input(" Ingrese el segundo número: "))#Aquí le pido al usuario el segundo número.
            break
        except ValueError: # Lo utilizo para que cuando me lance ese error, le muestre otro mas entendible y tenga la opcion de cambiarlo.
            print("\nLo siento, no se permite data basura.\nVuelva a intentarlo.\n")
            continue

            
    numero1cuadrado = numero1**2#Aquí elevo el primer número que me da el usuario al cuadrado.
    numero2cuadrado = numero2**2#Aquí elevo el segundo número que me da el usuario al cuadrado.
    operacion = (numero1cuadrado + numero2cuadrado)#Aquí es para que me sume los dos números ya elevados al cuadrado.
    raizOperacion = round(math.sqrt(operacion),2) # Utilizamos math.sqrt para sacar la raiz y round para redondearla a 2 decimales.
    
    #Salidas/proceso que el usuario verá.
    print("|----------------------------------------------|")
    print("\n El resultado de: ", str(f'{numero1:,}') + "^2 =", f'{numero1cuadrado:,}') #Aquí le muestra el mismo elevado al cuadrado.
    print("|----------------------------------------------|")
    print("\n El resultado de: ", str(f'{numero2:,}') + "^2 =", f'{numero2cuadrado:,}')#Aquí le muestra el mismo elevado al cuadrado.
    print("|----------------------------------------------|")
    print("\n La suma de ",f'{numero1cuadrado:,}',f'+ {numero2cuadrado:,} =', f'{operacion:,}') #Aquí le muestra la suma de los números cuadrados.
    print("|----------------------------------------------|")
    print("\n La raiz de ",f'{operacion:,} es: {raizOperacion:,}')#Aquí le muestra ya el resultado de el problema resuelto.
    print("|----------------------------------------------|")

    #========================== Agradecimiento por usar el programa =========================#  

    """
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

    print(em("""
*-----------------------------------------*
|  ¡Programa 2 Finalizado exitosamente! :smiling_face_with_smiling_eyes:|
*-----------------------------------------*
"""))
#========================== Fin Agradecimiento por usar el programa =========================#
programa2()