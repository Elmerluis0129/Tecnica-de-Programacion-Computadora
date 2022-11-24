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
