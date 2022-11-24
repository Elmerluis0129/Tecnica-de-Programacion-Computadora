import modulo_calculadora

def main():
	while True:
		print("1. Acelerar")
		print("2. Frenar")

		valor = int(input("> "))
		if valor == 1:
			c = modulo_calculadora.Carro(True)
			c.movilidad()
		else:
			c = modulo_calculadora.Carro(False)
			c.movilidad()



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nSaliendo...")
		exit()