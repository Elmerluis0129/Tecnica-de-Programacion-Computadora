print("Introduce dos números a comparar: ");
print();

num_uno = int(input("Introduce el primer número: "));
num_dos = int(input("Introduce el segundo número: "));

print("Los números a comparar son el: ", num_uno, " y el ", num_dos);

if num_uno != num_dos:
    print(num_uno, " no es igual a ", num_dos);
    
if num_uno > num_dos:
    print(num_uno, " es mayor a ", num_dos);
    
if num_uno < num_dos:
    print(num_uno, " es menor a ", num_dos);
    
if num_uno >= num_dos:
    print(num_uno, " es mayor o igual a ", num_dos);
    
if num_uno <= num_dos:
    print(num_uno, " es menor o igual a ", num_dos);
    
if num_uno == num_dos:
    print(num_uno, " es igual a ", num_dos);

print();
print("El programa ha finalizado correctamente.")
