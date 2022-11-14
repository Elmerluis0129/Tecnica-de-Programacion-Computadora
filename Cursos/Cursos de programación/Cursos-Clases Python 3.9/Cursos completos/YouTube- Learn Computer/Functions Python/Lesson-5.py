#built -in-functions. / Functions that are always available for use.
print("built -in-functions.")
name=input("Enter your name: ")
L=len(name)
print(name," has: ",L, " characters\n")

#function in module. / These same as built-in-functions but need to import module.
print("function in module.")
import math #Aquí importamos la librería de matemáticas a python.
a,b=5,3#Aquí podemos ver como el 5 se multiplicaría 3 veces por el mismo. (ejemplo: 5 * 5 * 5) / El 'int' es para que el resultado se convierta en entero.
c=int(math.pow(a,b)) #Esta librería funciona para multiplicar 'x' número por 'n' cantidad de veces
print("Multiplying: ",a, end=", ")
print( b, " times, that is: ",c, "\n")

#user defined functions. / These functions are defined by the programmers according to requirement.
#Example 1.
print("user defined functions.")
print("Example 1")
def sum(x,y):
    z=x+y
    return z

a,b=10,20
r=sum(a,b)
print(r, "\n")

#Example 2.
#Orden de ejecución: 1,2,5,8,9,5,6,7,9,10,2,3,4,10,11,12
print("Example 2") #Line 1
def find_cube(x): #Line 2
    cube=x*x*x #Line 3
    return cube #Line 4

def find_double(x): #Line 5
    db1=x*2 #Line 6
    return db1 #Line 7

a=5 #Line 8
d=find_double(a) #Line 9
c=find_cube(a) #Line 10
print(a, "double is: ", d) #Line 11
print(a ,"cube is: ", c) #Line 12




