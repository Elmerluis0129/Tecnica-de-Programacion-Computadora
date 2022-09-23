#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
#Elmer Saint-Hilare 21/1354

Lista = []
x = 1

print("*--------------------------------------------*")
print("|Ingresar las 5 palabras para crear la lista.|")
print("*--------------------------------------------*\n")

for n in range(5):
    if x == 1:
        Lista.append(input("Ingresar la primera palabra para la lista: "))
    elif x == 2:
        Lista.append(input("Ingresar la segunda palabra para la lista: "))
    elif x == 3:
        Lista.append(input("Ingresar la tercera palabra para la lista: "))
    elif x == 4:
        Lista.append(input("Ingresar la cuarta palabra para la lista: "))
    elif x == 5:
        Lista.append(input("Ingresar la quinta palabra para la lista: "))
        break
    x = x+1
    
buscarPalabra = input("Escriba la palabra que desea buscar: ")
VecesRepetida = Lista.count(buscarPalabra)

if VecesRepetida > 1:
    print("Las veces que la palabra: ","'",buscarPalabra,"'", "se repite es: ",VecesRepetida, "veces.")
elif VecesRepetida == 1:
    print("Las veces que la palabra: ","'",buscarPalabra,"'", "se repite es: ",VecesRepetida, "vez.")
else:
    print("Las veces que la palabra: ","'",buscarPalabra,"'", "se repite es: ",VecesRepetida, "veces.") #TODO Recuerda agregarle que si una palabra no se encuentra en la lista, se lo notifique al usuario.