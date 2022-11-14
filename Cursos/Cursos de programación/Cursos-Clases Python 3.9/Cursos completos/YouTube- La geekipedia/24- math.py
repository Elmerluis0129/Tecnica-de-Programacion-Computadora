import math

print("****************************************")
print("* Buscar la raíz cuadrada de un número *")
print("****************************************\n")

numero = int(input("Introduce un número por favor: "))
intentos = 0

while numero < 0:
	print("Lo siento, pero no puedo buscar una raíz cuadrada de un número negativo. Vuelve a intentarlo")

	if intentos == 2:
		print("Has consumido los 3 intentos permitidos. ¡El programa ha finalizado!")
		break;

	numero = int(input("Introduce un número por favor: "))
	if numero < 0:
		intentos=intentos+1

if intentos < 2:
	solucion=math.sqrt(numero)
	print("La raíz cuadrada de ", numero, " es: ", round(solucion, 2))
