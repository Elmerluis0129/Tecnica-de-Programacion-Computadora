class Carro(object):
	def __init__(self,m):
		self.color = "Color: Rojo"
		self.puertas = "Puertas: 4"
		self.marca = "Marca: Deportivo" 
		self.m = m

	def movilidad(self):
		if self.m == True:
			print("Carro acelerando")
		else:
			print("Carro frenando")

def main():
	while True:
		print("1. Acelerar")
		print("2. Frenar")

		valor = int(input("> "))
		if valor == 1:
			c = Carro(True)
			c.movilidad()
		else:
			c = Carro(False)
			c.movilidad()

if __name__ == "__main__":
	main()
