print("Calculador con una sola variable")
print()

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto")
print()

opcion = float(input("Introduce la opción deseada: "))

if opcion == 1:
    print("Elegiste Suma.")
    print()
    
#Proceso Suma
    
    numero = float(input("Ingresa el primer valor a sumar: "))
    numero += float(input("Ingresa el segundo valor a sumar: "))
    print("El resultado de tu suma es: ", round(numero,2))

    
elif opcion == 2:
    print("Elegiste Resta.")
    print()

#Proceso Resta
    
    numero = float(input("Ingresa el primer valor a restar: "))
    numero -= float(input("Ingresa el segundo valor a restar: "))
    print("El resultado de tu resta es: ", round(numero,2))


elif opcion == 3:
    print("Elegiste Multiplicación.")
    print()
    
#Proceso Multiplicación
    
    numero = float(input("Ingresa el primer valor a multiplicar: "))
    numero *= float(input("Ingresa el segundo valor a multiplicar: "))
    print("El resultado de tu multiplicación es: ", round(numero,2))

    
elif opcion == 4:
    print("Elegiste División.")
    print()
    
#Proceso División
    
    numero = float(input("Ingresa el primer valor a dividir: "))
    numero /= float(input("Ingresa el segundo valor a dividir: "))
    print("El resultado de tu división es: ",  round(numero,2))

    
elif opcion == 5:
    print("Elegiste División entera.")
    print()
    
#Proceso División entera
    
    numero = float(input("Ingresa el primer valor a dividir entero: "))
    numero //= float(input("Ingresa el segundo valor a dividir entero: "))
    print("El resultado de tu división entera es: ", round(numero,2))

    
elif opcion == 6:
    print("Elegiste Exponente.")
    print()
    
#Proceso Exponente
    
    numero = float(input("Ingresa el primer valor a exponenciar: "))
    numero **= float(input("Ingresa el segundo valor a exponenciar: "))
    print("El resultado de tu exponente es: ", round(numero,2))

    
elif opcion == 7:
    print("Elegiste Modulo o resto.")
    print()
    
#Proceso Modulo o resto
    
    numero = float(input("Ingresa el primer valor a sacar el modulo o resto: "))
    numero %= float(input("Ingresa el segundo valor a sacar el modulo o resto: "))
    print("El resultado de tu exponente es: ", round(numero,2))

    
else:
    print("La opción elegida no existe.")







    
