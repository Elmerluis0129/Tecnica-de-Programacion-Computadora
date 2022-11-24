# Clases padres
class Auto():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas") 

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas ")

def desplazamientoVehiculo(Vehiculo): # Aqui creamos la funcion desplazamientoVehiculo y le ponemos que argumento vehiculo.
	Vehiculo.desplazamiento() # Aqui al argumento que agregamos anteriormente, lo juntamos con desplazamiento.

# Polimorfismo:
miVehiculo = Camion() # Creamos la instancia dandole un tipo, en este caso es camion, puede ser cualquier otro tipo de clase, Auto, o Moto.
desplazamientoVehiculo(miVehiculo) # Aqui le decimos que la instancia miVehiculo es la respuesta que se debe guardar en el argumento que pide la funci[on desplazamientoVehiculo.
								   # De esta manera le hacemos instancia de que el desplazamiento que requiero, es el de la clase camion.

# Sin Polimorfismo:
miVehiculo2 = Auto()
miVehiculo2.desplazamiento()
