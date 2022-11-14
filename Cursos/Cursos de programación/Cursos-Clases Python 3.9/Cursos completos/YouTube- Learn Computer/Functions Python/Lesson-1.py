#Multiplicar un numero por el mismo numero, usando la función def.

#Ejemplo 1.  / Primera forma de multiplicar número por número.

def SQUARE(x):
    return x*x

a=5
print("El resultado es de: ", end=" ")
print(SQUARE(a))


#Ejemplo 2. / Segunda forma de multiplicar número por número.

def SQUARE(x):
    print(x*x)

a=5
print("El resultado es de: ", end=" ")
SQUARE(a)


#Ejemplo 3. / Aquí llamamos la función más de 1 vez, al mismo tiempo.

def SQUARE(x,y,z):
    print(x*x,y*y,z*z)

a,b,c=5,12,23
print("El resultado es de: ", end=" ")
SQUARE(a,b,c)


#Continuación del uso de la función, def.

#Aquí, solo le aplica la función a "a" una sola vez, ya que la función def, solo fue llamada una sola vez.

def change(x):
    x=x+10
    print(x)

a=10
print(a)
change(a) # Y es en este caso, unicamente, cuando es llamada la función.
print(a)

