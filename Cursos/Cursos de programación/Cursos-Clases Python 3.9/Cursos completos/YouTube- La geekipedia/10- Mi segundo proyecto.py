#Condicionales anidadas.

print("=========");
print("Conversor");
print("=========");

print("Menú de opciones");
print();
print("Presiona 1 para convertir de números a palabras.");
print("Presiona 2 para convertir de palabras a números.");
print();
opcion = int(input("¿Cuál opción eliges?: "));
print();

if opcion == 1:
    print("Conversor de números a palabras");
    print();
    opcion_uno = int(input("¿Cuál es el número que deseas convertir a palabra?: "));
    if opcion_uno == 1:
        print("El número es 'UNO'");
    elif opcion_uno == 2:
        print("El número es 'DOS'");
    elif opcion_uno == 3:
        print("El número es 'TRES'");
    elif opcion_uno == 4:
        print("El número es 'CUATRO'");
    elif opcion_uno == 5:
        print("El número es 'CINCO'");
    elif opcion_uno == 6:
        print("El número es 'SEIS'");
    elif opcion_uno == 7:
        print("El número es 'SIETE'");
    elif opcion_uno == 8:
        print("El número es 'OCHO'");
    elif opcion_uno == 9:
        print("El número es 'NUEVE'");
    elif opcion_uno == 10:
        print("El número es 'DIEZ'");
    elif opcion_uno == 11:
        print("El número es 'ONCE'");
    elif opcion_uno == 12:
        print("El número es 'DOCE'");
    elif opcion_uno == 13:
        print("El número es 'TRECE'");
    elif opcion_uno == 14:
        print("El número es 'CATORCE'");
    elif opcion_uno == 15:
        print("El número es 'QUINCE'");
    elif opcion_uno == 16:
        print("El número es 'DIECISEIS'");
    elif opcion_uno == 17:
        print("El número es 'DIECISIETE'");
    elif opcion_uno == 18:
        print("El número es 'DIECIOCHO'");
    elif opcion_uno == 19:
        print("El número es 'DIECINUEVE'");
    elif opcion_uno == 20:
        print("El número es 'VEINTE'");
    elif opcion_uno == 21:
        print("El número es 'VEINTE Y UNO'");
    elif opcion_uno == 22:
        print("El número es 'VEINTE Y DOS'");
    elif opcion_uno == 23:
        print("El número es 'VEINTE Y TRES'");
    elif opcion_uno == 24:
        print("El número es 'VEINTE Y CUATRO'");
    elif opcion_uno == 25:
        print("El número es 'VEINTE Y CINCO'");
    else:
        print("Este programa solo imprime hasta el número 25(VEINTE Y CINCO). ");
        
elif opcion == 2:
    print("Conversor de palabras a números.");
    print();
    opcion_dos = input("¿Cuál es la palabra que quieres convertir a número: ");
    opcion_dos = opcion_dos.lower()
    
    if opcion_dos == "uno":
        print("La palabra es: '1'");
    elif opcion_dos == "dos":
        print("La palabra es: '2'");
    elif opcion_dos == "tres":
        print("La palabra es: '3'");
    elif opcion_dos == "cuatro":
        print("La palabra es: '4'");
    elif opcion_dos == "cinco":
        print("La palabra es: '5'");
    elif opcion_dos == "seis":
        print("La palabra es: '6'");
    elif opcion_dos == "siete":
        print("La palabra es: '7'");
    elif opcion_dos == "ocho":
        print("La palabra es: '8'");
    elif opcion_dos == "nueve":
        print("La palabra es: '9'");
    elif opcion_dos == "diez":
        print("La palabra es: '10'");
    elif opcion_dos == "once":
        print("La palabra es: '11'");
    elif opcion_dos == "doce":
        print("La palabra es: '12'");
    elif opcion_dos == "trece":
        print("La palabra es: '13'");
    elif opcion_dos == "catorce":
        print("La palabra es: '14'");
    elif opcion_dos == "quince":
        print("La palabra es: '15'");
    elif opcion_dos == "dieciseis":
        print("La palabra es: '16'");
    elif opcion_dos == "diecisiete":
        print("La palabra es: '17'");
    elif opcion_dos == "dieciocho":
        print("La palabra es: '18'");
    elif opcion_dos == "diecinueve":
        print("La palabra es: '19'");
    elif opcion_dos == "veinte":
        print("La palabra es: '20'");
    elif opcion_dos == "veinte y uno":
        print("La palabra es: '21'");
    elif opcion_dos == "veinte y dos":
        print("La palabra es: '22'");
    elif opcion_dos == "veinte y tres":
        print("La palabra es: '23'");
    elif opcion_dos == "veinte y cuatro":
        print("La palabra es: '24'");
    elif opcion_dos == "veinte y cinco":
        print("La palabra es: '25'");
    else:
        print("Este programa solo convierte hasta el número veinte y cinco(25). ");
else:
    print("Opción no disponible.");

print("Fin.");
    

