#Modificando los valores de una misma lista.
#List are mutable in python, but, string aren't mutable in python.

s="welcome, elmer"
print(s)

L=[10,20,5,30] #Lista principal
print(L, " Lista sin modificar\n")

L[0]=L[0]+20 #Primera modificación
print(L, " Lista, primera modificación\n")

L[1]=L[1]+45 #Segunda modificación
print(L, " Lista, segunda modificación\n")

L[2]=L[2]+19 #Tercera modificación
print(L, " Lista, tercera modificación\n")

L[3]=L[3]+17 #Cuarta modificación
print(L, " Lista, cuarta modificación\n")

#Otro ejemplo:

print("Otro ejemplo: \n")
def change(x):
    x[1]=x[1]+20
    print(x)
    print("id de x: ", id(x)) # Aquí simplemente estamos pidiendo que muestre la ubicación o mejor conocido como id de nuestra función llamada "x"

a=[10,20,30,40]
print(a)
change(a) #En este llamado, afecta también la linea de código de abajo.
print(a)  #De modo que, esta linea también sale con el resultado de la lista x.
print("id de a: ", id(a)) # Aquí simplemente estamos pidiendo que muestre la ubicación o mejor conocido como id de nuestra función llamada "a"

