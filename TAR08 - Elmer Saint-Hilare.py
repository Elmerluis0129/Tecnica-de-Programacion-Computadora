#Escriba un programa que, mediante una función, retorne las tablas de multiplicar del n al m.

#Ejemplo:

#Ingrese el número por el que comenzarán a mostrarse las tablas: 1

#Ingrese el número por el que terminarán a mostrarse las tablas: 3

print("""
*--------------------*  
|Tabla de multiplicar|
*--------------------*
\n""")#Decoración.

#==========================Inicio/Final=========================#   
Inicio = int(input("Escribe un número para comenzar la tabla: ")) 
Final = int(input("Escribe un número para terminar la tabla: ")) 
print("\n\n")#Saltos de líneas.

j = 0
for d in range(0, 10):
    j = j + 1

#==========================Función=========================#
def multiplicar (x):
    print("Tabla del: ", Inicio)
    for i in range(0, 11):
        operación = x * i
        print(Inicio, "*", i ,"=", operación)
    print("\n")
    
    #for m in range(0,10):
        #m = m + 1
    
    #print((Inicio+1) * 0, "\n", (Inicio+1) * 1, "\n", (Inicio+1) * 2, "\n", (Inicio+1) * 3, "\n", (Inicio+1) * 4, "\n", (Inicio+1) * 5,"\n", (Inicio+1) * 6, "\n", (Inicio+1) * 7, (Inicio+1) * 8,"\n", (Inicio+1) * 9, "\n", (Inicio+1) * 10)

    
def multiplicar2 (y):
    print("Tabla del: ", Final)
    for a in range(0,11):
        operación1 = y * a
        print(Final, "*", a ,"=", operación1)
        
def multiplicar3 (j):
    for a in range(0, 11):
        operación = a * j
        print((Inicio+1), "*", a ,"=", operación)
    print("\n")
    
    
    



multiplicar(Inicio)
while j == (Final - 1):
    multiplicar3(Inicio+1)
if j != (Final - 1):
    multiplicar2(Final)
else:
    print("no cumple")

#TODO RECORDAR PONER QUE IMPRIMA LAS TABLAS DEL MEDIO DEL INICIO Y EL FINAL