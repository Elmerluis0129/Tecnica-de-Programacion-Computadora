#Conjución

print("Conjución (and)")
print()

num_uno = int(input("Escribe un número entre 2 y 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número que has marcado es correcto")
    print()
else:
    print("El número que has marcado no es correcto")
    print()

#Disyunción

print("Disyunción(or)")
print()

palabra = input('Para cumplir con la condición escribe "Si" o "Yes": ' )

if palabra == "Si" or palabra == "Yes":
    print("La condición se ha cumplido")
    print()
else:
    print("La condición no se ha cumplido")

#Negación

print("Negación(not)")
print()

num_uno = int(input("Escribe un número igual a 6: "))

if not num_uno == 6:
    print("El número que has marcado no es igual a 6")
else:
    print("El número que has marcado si es igual a 6")
    
