#Métodos de cadenas (Manipulación de la misma) / Documentación de los métodos de cadenas: https://recursospython.com/guias-y-manuales/30-metodos-de-las-cadenas/

nombre = input("Escribe tu nombre: ")

print("Mayusculas: ",nombre.upper()) #Convierte todas en mayusculas
print("Minusculas: ",nombre.lower()) #Convierte todas en minusculas
print("Primera letra mayusculas: ",nombre.capitalize()) #Convierte la primera en mayusculas
print("Aparece: ",nombre.count("Elmer"), "Vez/veces") #Sirve para contar cuantas veces aparece una letra o una cadena de caracteres
print("Aparece en la posición: ",nombre.find("e")) #Sirve para encontrar una letra o una cadena de caracteres
print("¿Es dígito?: ",nombre.isdigit()) #Sirve para saber si el valor es digito(númerico)
#print("¿Es alfanúmerico?: ",nombre.isalum()) #Sirve para saber si el valor es alphanúmerico o no (Caracteres y numeros)
print("¿Es alpha(letra/s)?: ",nombre.isalpha()) #Sirve para saber si el valor es aplha (Caracteres)
print("Separado: ",nombre.split()) #Sirve para separar por palabras utilizando espacios
print("Sin espacio: ",nombre.strip()) #Sirve para borrar esapcios sobrantes, al principio y al final
print("Reemplazo: ",nombre.replace(nombre, "elmer")) #Sirve para remplazar una letra por otra, o una cadena por otra
print("Aparece en la posición: ",nombre.rfind("e")) #Va de la mano con find, la diferencia es que este cuenta de derecha a izquierda
print("Izquierda: ",nombre.ljust(20, "*")) #Sirve para poner el valor a la izquierda, y rellenar los espacios con el segundo parametro (*)
print("Centro: ",nombre.center(20, "*")) #Sirve para poner el valor en el centro, y rellenar los espacios con el segundo parametro (*)
print("Derecha: ",nombre.rjust(20, "*")) #Sirve para poner el valor a la derecha, y rellenar los espacios con el segundo parametro (*)
print("Intercambio: ", nombre.swapcase()) #Sirve para intercambiar las mayusculas por las minusculas y viceversa


