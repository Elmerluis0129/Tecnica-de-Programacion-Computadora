print("*------------------------------*")
print("* Secuencia de números mayores *")
print("*------------------------------*")	

num1 = int(input("Introduce el #1: "))
num2 = int(input("Introduce el #2: "))
numero1 = 3
numero2 = 4

if num1 == num2:
	print("""Lo siento, pero el número {} no es mayor al número {}
¡El programa ha finalizado!""".format(num1, num2))

if num1 > num2:
	print("""Recuerda que sólo puedes ir introduciendo un número más alto que el anterior.
el {} no es más alto que el {} 
¡El programa ha finalizado!""".format(num2, num1))

while num1 < num2:
	num1 = int(input("Introduce el #{}: ".format(numero1)))
	numero1 = numero1 + 1
	num2 = int(input("Introduce el #{}: ".format(numero2)))
	numero2 = numero2 + 1

	if num1 > num2:
		print("""Recuerda que sólo puedes ir introduciendo un número más alto que el anterior.
el {} no es más alto que el {} 
¡El programa ha finalizado!""".format(num2, num1))
		break;
	if num1 == num2:
		print("""Lo siento, pero el número {} no es mayor al número {}
¡El programa ha finalizado!""".format(num1, num2))

