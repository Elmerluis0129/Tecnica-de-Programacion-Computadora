print("**************************************************************************")
print("* Pograma para determinar ¿Cuál es el número más grande de tres números? *")
print("**************************************************************************")
print()

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
guardar = 0

if numero1 > numero2 and numero1 > numero3:
    print("El número ", numero1, " es mayor a los otros números.")
elif numero2 > numero3:
    print("El número ", numero2, " es mayor a los otros números.")
else:
    print("El número ", numero3, " es mayor a los otros números.")
