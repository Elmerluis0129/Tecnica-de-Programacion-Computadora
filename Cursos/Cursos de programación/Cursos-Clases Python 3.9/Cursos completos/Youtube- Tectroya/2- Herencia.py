#Clase Padre / Super Clase
class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca     = marca
		self.modelo    = modelo
		self.arranca   = False
		self.acelera   = False
		self.frena     = False
		self.encendido = False

	def encender(self):
		self.encendido = True	

	def arrancar(self):
		self.arranca = True

	def acelerar(self):
		self.acelera = True

	def frenar(self):
		self.frena = True

	def estado(self):
		print("Marca> ", self.marca, "\nModelo> ", self.modelo, "\nEncendido> ", self.encendido, "\nArranca> ", self.arranca, "\nAcelera> ", self.acelera, "\nFrena> ", self.frena)

class Moto(Vehiculo): # Aqui le heredamos a la clase moto, la super clase de Vehiculo, el cual tiene su propio constructor que son la marca y el modelo, tambien hereda todo lo que esta adentro de Vehiculo
	def calibra(self, calibrando): # Funcion
		self.calibrando = calibrando
		if self.calibrando and self.encendido and self.arranca and self.acelera:
			print("Estoy calibrando en la moto")
		else:
			print("No estoy calibrando en la moto")


# Clase Hija / Clases derivadas
class Furgon(Vehiculo):  # Aqui le heredamos a la clase Furgon, la super clase de Vehiculo, el cual tiene su propio constructor que son la marca y el modelo, tambien hereda todo lo que esta adentro de la Super clase Vehiculo

	def carga(self, carga):
		self.cargado = carga
		if self.cargado:
			print("El furgon está cargado")
		else:
			print("El furgon no está cargado")

# Clase Padre / Super Clase 
class VElectrico(Vehiculo):   # Aqui le heredamos a la Super clase VElectrico, la super clase de Vehiculo, el cual tiene su propio constructor que son la marca y el modelo, tambien hereda todo lo que esta adentro de la Super clase Vehiculo
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo) # Aqui llamamos la Sup. Clase Vehiculo con la palabra reservada "super()", especificando el constructor de la misma y pidiendole tanto la marca como el modelo que tiene.
		self.autonomía = 100

	def cargaEnergia(self):
		self.cargado = True

	def estado(self):
		super().estado()
		print("Autonomía> ", self.autonomía)


# Clase Hija / Clases derivadas
class BicicletaElectrica(VElectrico, Vehiculo): # Aqui hereda de dos super clases, Vehiculo y VElectrico
	pass
		

# Instancias
miMoto = Moto("Yamaha", "115")
miMoto.encender()
miMoto.estado()
print(miMoto.calibra(1))

print("----------------------------Continuación----------------------------")

miFurgon = Furgon("Renault", "Kangoo")
miFurgon.encender()
miFurgon.arrancar()
miFurgon.estado()
print(miFurgon.carga(0))

print("----------------------------Continuación----------------------------")

miBici = BicicletaElectrica("Mongoo", "Aro 20")
miBici.estado()