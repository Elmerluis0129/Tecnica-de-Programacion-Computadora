"""
Realizar un programa que permita la ejecución de todos los ejercicios que se han hecho hasta el momento (TAR01 - TAR12).

Indicaciones:

El programa debe tener un menú que permita seleccionar el ejercicio que se desea ejecutar.
Luego de seleccionar un ejercicio, además de su ejecución (entradas, y demás funcionalidades), se debe mostrar el enunciado del mismo. (Esto debe aparecer arriba).
Se debe hacer uso de módulos: los ejercicios deben ser importados desde el programa principal.
Una vez terminada la ejecución de un ejercicio, el programa debe permitir volver al menú principal o terminar la ejecución de todo el programa.
El programa debe controlar la captura de data basura.
Recomendación: para aquellos ejercicios que no completaron correctamente y que tienen observaciones de mejora, favor de corregirlos para que se ejecuten 100% correctos.

Elmer Saint-Hilare 21-1354
"""

# ================= Importaciones ================= #
"""
Aquí importo mis 12 programas, para tener acceso a los mismo con su respectivos nombres, del ms1 al ms12.
"""
from Módulos import TAR01_Elmer_Saint_Hilare as ms1
from Módulos import TAR02_Elmer_Saint_Hilare as ms2
from Módulos import TAR03_Elmer_Saint_Hilare as ms3
from Módulos import TAR04_Elmer_Saint_Hilare as ms4
from Módulos import TAR05_Elmer_Saint_Hilare as ms5
from Módulos import TAR06_Elmer_Saint_Hilare as ms6
from Módulos import TAR07_Elmer_Saint_Hilare as ms7
from Módulos import TAR08_Elmer_Saint_Hilare as ms8
from Módulos import TAR09_Elmer_Saint_Hilare as ms9
from Módulos import TAR10_Elmer_Saint_Hilare as ms10
from Módulos import TAR11_Elmer_Saint_Hilare as ms11
from Módulos import TAR12_Elmer_Saint_Hilare as ms12
# =============== Fin Importaciones =============== #

# ================ Importando para decorar ================ #
"""
Aquí importo para poder decorar el codigo, como en este caso para usar emojis.
"""
from emoji import emojize as em

"""
Aquí lo importo para usar la función sleep y poder controlar la velocidad de iteración del bucle for.
"""
import time
# ============== Fin Importando para decorar ============== #

# ===== Variables generaeles ===== #
mensaje = "Recuerda que si quieres ver el menú de opciones solo tienes que escribir: \"13\""
control = 1
# === Fin Variables generaeles === #

# ================ Barra de porcentaje ================ #
"""
Aquí declaro mi limite una función, que es la que se encarga de hacer los cálculos de la barra.
Con el for es para darle formato a la barra de carga, de tal manera que vaya haciendolo con un tiempo de 0,7 por iteración.

Con cada condicional en la barra formato, es para saber que barra va en cada proceso.
Tengo que cuando reciba 1, es para la barra de inicio del programa.
Tengo que cuando reciba 2, es para la barra de carga de los programas(Tareas).
Y en caso de ninguno, pues la barra de fin del programa.
"""
limite = 50

def barraProgreso(segmento, total, longitud):
    porcentaje = segmento / total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{'+' * completado}{'-' * restante}{porcentaje:.0%}]"
    return barra

def barraFormato(decision):
    if decision == 1:
        input("\nPresione Enter para iniciar el programa... \n")
        print("\nCargando... Por favor espere.")
        for i in range(limite+1):
            time.sleep(0.07)
            print(barraProgreso(i, limite, 50), end = "\r")
        print("\n")
        
    elif decision == 2:
        print("\nCargando... Por favor espere.")
        for i in range(limite+1):
            time.sleep(0.01)
            print(barraProgreso(i, limite, 50), end = "\r")
        control = 1
    
    else:
        print("\nCerrando el programa general...")
        for i in range(limite+1):
            time.sleep(0.02)
            print(barraProgreso(i, limite, 50), end = "\r")
        print("\n")

barraFormato(1)
    
# ============== Fin Barra de porcentaje ============== #

# ================= Menú de opciones ================= #
"""
Muestro por pantalla mi menú de opciones cada vez que lo llamo.
"""
def menuOpciones():
    print("""
*--------------------------------------*
|          Menú de opciones            |
*--------------------------------------*
|1.-| Operaciones Básicas.             |
|--------------------------------------|
|2.-| Entrada teclado.                 |
|--------------------------------------|
|3.-| Precio de energía eléctrica.     |
|--------------------------------------|
|4.-| Veces que se repite una palabra. |
|--------------------------------------|
|5.-| Números de lotería.              |
|--------------------------------------|
|6.-| Préstamos usando while.          |
|--------------------------------------|
|7.-| Lista de caracteres usando while.|
|--------------------------------------|
|8.-| Tablas de multiplicar.           |
|--------------------------------------|
|9.-| Primer caracter que no se repite.|
|--------------------------------------|
|10.-| Más funciones.                  |
|--------------------------------------|
|11.-| Sets a partir de listas.        |
|--------------------------------------|
|12.-| Los viajeros.                   |
|--------------------------------------|
|13.-| Mostrar Menú de opciones.       |
|--------------------------------------|
|14.-| Cerrar programa general.        |
*--------------------------------------*
""")
menuOpciones()
# =============== Fin Menú de opciones =============== #

while True:
    if control == 3: break
    elif control == 1: eleccion = input("¿Qué programa desea ejecutar? \n> ")
    
    # ==== Condicionales - Control de programas ==== #
    """
    Aquí controlo cual programa se va ejecutar, según el que seleccione el usuario.
    Aquí también controlo la data basura, para evitar que ponga algo no esperado, en caso de, se lo notifica y espera la corrección del mismo.
    """
    if eleccion == "1":    barraFormato(2),  print("\n\nHaz elegido el programa 1: Operaciones Básicas.\n"),              ms1.programa1(),   print(mensaje)
    elif eleccion == "2":  barraFormato(2),  print("\n\nHaz elegido el programa 2: Entrada teclado.\n"),                  ms2.programa2(),   print(mensaje)   
    elif eleccion == "3":  barraFormato(2),  print("\n\nHaz elegido el programa 3: Precio energía eléctrica.\n"),         ms3.programa3(),   print(mensaje)  
    elif eleccion == "4":  barraFormato(2),  print("\n\nHaz elegido el programa 4: Veces que se repite una palabra.\n"),  ms4.programa4(),   print(mensaje)
    elif eleccion == "5":  barraFormato(2),  print("\n\nHaz elegido el programa 5: Números de lotería.\n"),               ms5.programa5(),   print(mensaje)
    elif eleccion == "6":  barraFormato(2),  print("\n\nHaz elegido el programa 6: Préstamos usando while.\n"),           ms6.programa6(),   print(mensaje)
    elif eleccion == "7":  barraFormato(2),  print("\n\nHaz elegido el programa 7: Lista de caracteres usando while.\n"), ms7.programa7(),   print(mensaje)
    elif eleccion == "8":  barraFormato(2),  print("\n\nHaz elegido el programa 8: Tablas de multiplicar.\n"),            ms8.programa8(),   print(mensaje)
    elif eleccion == "9":  barraFormato(2),  print("\n\nHaz elegido el programa 9: Primer caracter que no se repite.\n"), ms9.programa9(),   print(mensaje)
    elif eleccion == "10": barraFormato(2),  print("\n\nHaz elegido el programa 10: Más funciones.\n"),                   ms10.programa10(), print(mensaje)
    elif eleccion == "11": barraFormato(2),  print("\n\nHaz elegido el programa 11: Sets a partir de listas.\n"),         ms11.programa11(), print(mensaje)
    elif eleccion == "12": barraFormato(2),  print("\n\nHaz elegido el programa 12: Los viajeros.\n"),                    ms12.programa12(), print(mensaje)
    elif eleccion == "13": barraFormato(2),  menuOpciones()
    elif eleccion == "14":
        barraFormato(0)
        break
    elif eleccion != "14":
        while True:
            print("Lo siento, lo que haz introducido no va acorde con los números del menú de opciones.")
            print("Intenta de nuevo.\n")
            eleccion = input("¿Qué programa desea ejecutar? \n> ")
            if eleccion == "1"  or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13":
                control = "1"
                break
            elif eleccion == "14":
                barraFormato(0)
                control = 3
                break     
        continue
    control = 1
    # == Fin Condicionales - Control de programas == #
    
            
# ========================== Agradecimiento por usar el programa ========================= #  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print(em("""
*----------------------------------------------------------------------------------*
| ¡Muchas gracias por utilizar mi programa! :thumbs_up: / By: Elmer Saint-Hilare 21-1354 :OK_hand: |
*----------------------------------------------------------------------------------*
"""))
# ========================== Fin Agradecimiento por usar el programa ========================= #