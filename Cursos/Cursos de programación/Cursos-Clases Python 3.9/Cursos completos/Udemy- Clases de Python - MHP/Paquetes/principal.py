import Paquete1.calculadora_modulo as calculadora

def main():
	while True:
		print("1. Acelerar")
		print("2. Frenar")

		valor = int(input("> "))
		if valor == 1:
			c = calculadora.Carro(True)
			c.movilidad()
		else:
			c = calculadora.Carro(False)
			c.movilidad()



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nSaliendo...")
		exit()