"""
Escriba un programa que, mediante una función, retorne las tablas de multiplicar del n al m.
Ejemplo:
Ingrese el número por el que comenzarán a mostrarse las tablas: 1.
Ingrese el número por el que terminarán a mostrarse las tablas: 3.
Elmer Saint-Hilare 21-1354.
"""

#========================== Nombre programa =========================# 
"""
Aquí es para imprimir el nombre del programa.
"""
print("""
*--------------------*  
|Tabla de multiplicar|
*--------------------*
\n""")
#========================== Fin Nombre programa =========================#

#========================== Inicio/Final =========================#  

"""
Aquí declaro mis variables inicio y fin, a las cuales le doy de valor una entrada que el usuario procederá a darme.
Y un salto de línea para que no salga pegado.
"""

Inicio = int(input("Escribe un número para comenzar la tabla: "))
Final = int(input("Escribe un número para terminar la tabla: ")) 
print("\n")
#========================== Fin Inicio/Final =========================# 

#========================== Funciones =========================#

"""
En las funciones las utilizo para reutilizar la lógica n veces sin necesidad de repetir las líneas de códigos n veces.
Aquí consta de 3 funciones: 
-La primera (Inicio) se encarga de realizar la tabla del número que le indique el usuario como inicio.
-La segunda (Desarrollo) se encarga de realizar las tablas que quedan de por medio de la tabla inicio y fin.
-La tercera (Final) se encarga de realizar la tabla del número que le indique el usuario como fin.

Aquí también le agrego lo que son los marcadores de inicio de la tabla y final de la tabla.
"""

#----- Función Inicio -----#
def multiplicar (x):
    print("""
*--------------*
|Tabla del:""", Inicio, """ | 
*--------------*
""")
    for i in range(0, 11):
        operación = x * i
        print(Inicio, "*", i ,"=", operación)
    
    print("""
*------------------*
|Fin tabla del:""", Inicio, """ | 
*------------------*
""")
#----- Fin Función Inicio -----#

#----- Función Desarrollo -----#         
def multiplicar3 (j):
    print("""
*--------------*
|Tabla del:""", Inicio+n, """ | 
*--------------*
""")
    for a in range(0, 11):
        operación2 = a * j
        print((Inicio+n), "*", a ,"=", operación2)
        
    print("""
*------------------*
|Fin tabla del:""", Inicio+n, """ | 
*------------------*
""")
#----- Fin Función Desarrollo -----# 

#----- Función Final -----# 
def multiplicar2 (y):
    print("""
*--------------*
|Tabla del:""", Final, """ | 
*--------------*
""")
    for a in range(0,11):
        operación1 = y * a
        print(Final, "*", a ,"=", operación1)
        
    print("""
*------------------*
|Fin tabla del:""", Final, """ | 
*------------------*
""")
#----- Fin Función Final -----# 

#========================== Fin Funciones =========================#

#========================== Lógica para imprimir las tablas n veces =========================#

"""
Aquí es dónde está la magía del código, está compuesto por un while que es el que se encarga de ir llamando las funciones en orden.
Primero me llama la función Inicio, que se encarga de iniciar con la tabla que el usuario quiere.
Después entra al while y lo ejecuta hasta que la función Desarrollo, que en este caso va imprimir la multiplicación de las tablas hasta que llegue el turno de llamar a la última función.
"""
  
n = 1
multiplicar(Inicio)
while True:
    multiplicar3(Inicio+n)
    
    if (Final - 1) == Inicio + n:
        multiplicar2(Final)
        break
    elif (Final) == Inicio + n:
        break
    n = n + 1
    continue
    
#========================== Fin Lógica para imprimir las tablas n veces =========================# 

#========================== Agradecimiento por usar el programa =========================#  

"""
Aquí imprimo por pantalla el agradecimiento y por quién fue creado, en este caso por mi.
"""

print("""
*----------------------------------------------------------------------------*
|  ¡Programa 8 Finalizado exitosamente! / By: Elmer Saint-Hilare 21-1354     |
*----------------------------------------------------------------------------*
""")
#========================== Fin Agradecimiento por usar el programa =========================#