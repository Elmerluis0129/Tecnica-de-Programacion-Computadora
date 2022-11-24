import pickle


#Lineas de codigos de mi proyecto vehiculos
class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca      = marca
		self.modelo     = modelo
		self.arranca    = False
		self.acelera    = False
		self.frena      = False
		self.reduciendo = False
		self.velocidadA = False
		self.apagar     = False
		self.encender   = False
		self.velocidad1 = 20
		self.velocidad2 = 40
		self.velocidad3 = 70
		self.reduce1    = self.velocidad1 - 10
		self.reduce2    = self.velocidad2 - 20
		self.reduce3    = self.velocidad3 - 30


	def estado(self):
		print(">Marca: ", self.marca, "\n>Modelo: ", self.modelo, "\n>Arranca: ", self.arranca, "\n>Acelera:", self.acelera, "\n>Frena: ", self.frena)


#Lista de objetos codificados en codigo binario
#coche1 = Vehiculo("Mazda", "MX5")
#coche2 = Vehiculo("Toyota", "Camry")
#coche3 = Vehiculo("Hyundai", "Megane")

#coches = [coche1, coche2, coche3]

#ficheroBinario = open("los_coches", "wb")
#pickle.dump(coches, ficheroBinario) #Volcamos nuestras variables
#ficheroBinario.close()
#del(ficheroBinario) #Con esto eliminamos el archivo de la memoria de la pc

#/------------------------------------------------------------------------------------------------------------------\#

#Lineas de codigo para ver el contenido de la lista de objetos que estan codificados en codigo binario
fichero = open("los_coches", "rb")
miscoches = pickle.load(fichero)
fichero.close()
for c in miscoches:
	print(c.estado())