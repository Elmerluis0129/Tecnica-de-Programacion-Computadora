eleccion = int(input("¿En qué vehiculo vas a salir?\n1.- Camion\n2.- Auto familiar\n3.- Helicoptero\n4.- Moto electrica\n> "))
if eleccion == 1:
	usando = "Camion"
elif eleccion == 2:
	usando = "Auto familiar"
elif eleccion == 3:
	usando = "Helicoptero"
elif eleccion == 4:
	usando = "Moto electrica"

class Vehiculo():
	def __init__(self, marca, modelo):
		self.marca      = marca
		self.modelo     = modelo
		self.arranca    = True
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

#Arranque
	def arranco(self, x):
		self.arranco = x
		if self.arranco and eleccion != 4 and eleccion : 
			print("Montandose, encendiendo y arrancando el " + usando)
			print("Velocidad actual: ", self.velocidad1)
		elif self.arranco and eleccion == 4: 
			print("Montandose, encendiendo y arrancando la " + usando)
			self.velocidadA = 20
		m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
		if m == 1 and self.velocidadA == 20: 
			self.acelero1()
		elif m == 1 and self.velocidadA == 40: 
			self.acelero2()
		elif m == 2: 
			deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))

			if deteniendo == 1: 
				self.freno()
			while deteniendo == 2: 
				print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
				self.velocidadA = 20
		r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		if r == 1: 
			self.acelero()
		elif r == 2 and self.velocidadA == 70: 
			self.reduciendo3()
		elif r == 2 and self.velocidadA == 40: 
			self.reduciendo2()
		elif r == 2 and self.velocidadA == 20: 
			self.reduciendo1()
		elif r == 3: 
			self.freno()
		else: 
			print("Esa opción no está en el menú")

	def arranco1(self):
		print("Arrancando...")
		print("Velocidad actual: ", self.velocidad1)
		self.velocidadA = 20
		m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
		if m == 1 and self.velocidadA == 20: 
			self.acelero1()
		elif m == 1 and self.velocidadA == 40:
			self.acelero2()
		elif m == 2: 
			deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
		if deteniendo == 1: 
			self.freno()
		while deteniendo == 2:
			print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
			self.velocidadA = 20
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if r == 1: 
				self.acelero()
			elif r == 2 and self.velocidadA == 70: 
				self.reduciendo3()
			elif r == 2 and self.velocidadA == 40: 
				self.reduciendo2()
			elif r == 2 and self.velocidadA == 20: 
				self.reduciendo1()
			elif r == 3: 
				self.freno()
			else: 
				print("Esa opción no está en el menú")

#Aceleracion
	def acelero(self):
		print("""Acelerando...\nVelocidad actual: """, (self.velocidad1) , """km/h\n""")
		self.velocidadA = 20
		l = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
		if l == 1 and self.velocidadA == 20: 

			self.acelero1()
		elif l == 1 and self.velocidadA == 40: 

			self.acelero2()
		elif l == 2 and self.velocidadA == 70: 

			self.reduciendo3()
		elif l == 2 and self.velocidadA == 40: 

			self.reduciendo2()
		elif l == 2 and self.velocidadA == 20: 

			self.reduciendo1()
		elif l == 3: 

			self.freno()
		elif l == 3: 

			self.freno()
		else: 

			print("Esa opción no está en el menú")

	def acelero1(self):
		print("""Acelerando...\nVelocidad actual: """, (self.velocidad2) , """km/h\n""")
		self.velocidadA = 40
		a = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
		if a == 1 and self.velocidadA == 40: 
			self.acelero2()
		elif a == 1 and self.velocidadA == 20: 
			self.acelero1()
		elif a == 2 and self.velocidadA == 70: 
			self.reduciendo3()
		elif a == 2 and self.velocidadA == 40: 
			self.reduciendo2()
		elif a == 2 and self.velocidadA == 20: 
			self.reduciendo1()
		elif a == 3: 
			self.freno()
		else: 
			print("Esa opción no está en el menú")

	def acelero2(self):
		print("""Acelerando...\nVelocidad máxima alcanzada: """, (self.velocidad3) , """km/h\n""")
		self.velocidadA = 70
		b = int(input("""¿Qué deseas hacer? \n1.-Reducir la velocidad \n2.-Detenerte por completo\n> """))
		if b == 1 and self.velocidadA == 70: 
			self.reduciendo3()
		elif b == 1 and self.velocidadA == 40: 
			self.reduciendo2()
		elif b == 1 and self.velocidadA == 20: 
			self.reduciendo1()
		elif b == 2: 
			self.freno() 
		else: 
			print("Esa opción no está en el menú")

#Reduccion de velocidad
	def reduciendo1(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce1) , "km/h\n")
		self.velocidadA = 10
		if self.velocidadA == 20: 
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		elif self.velocidadA <= 15: 
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Detenerte por completo\n> "))
		if n == 1: 
			self.acelero()
		elif n == 2: 

			self.freno()
		else: 
			print("Esa opción no está en el menú")

	def reduciendo2(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce2) , "km/h\n")
		self.velocidadA = 20
		n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		if n == 1 and self.velocidadA == 20: 
			self.acelero1()
		elif n == 1 and self.velocidadA == 40: 
			self.acelero2()
		elif n == 2 and self.velocidadA >= 70: 
			self.reduciendo3()
		elif n == 2: 
			self.reduciendo1()
		elif n == 3: 
			self.freno()
		else: 
			print("Esa opción no está en el menú")

	def reduciendo3(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce3) , "km/h\n")
		self.velocidadA = 40
		n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		if n == 1 and self.velocidadA == 20: 
			self.acelero1()
		elif n == 1 and self.velocidadA == 40: 
			self.acelero2()
		elif n == 2: 
			self.reduciendo1()
		elif n == 3: 
			self.freno()
		else: 
			print("Esa opción no está en el menú")

#Freno
	def freno(self):
		print("""De acuerdo\n Frenando...\n Velocidad actual:""", (self.velocidadA - self.velocidadA), """km/h\n""")
		d = int(input("""¿Qué deseas hacer? \n1.-Apagar \n2.-Arrancar\n> """))
		if d == 1: 
			self.apagandom()
		elif d == 2: 
			self.arranco1()
		else: 
			print("Esa opción no está en el menú")

#Apagado
	def apagandom(self):
		f = int(input("De acuerdo\n Apagando...\n ¿Qué deseas hacer? \n1.-Encender y arrancar \n2.-Desmontarse\n> "))
		if f == 1: 
			self.arranco1()
		elif f == 2: 
			print("Desmontandose...")
			exit()
		else: 
			print("Esa opción no está en el menú")

#Estado del vehiculo	
	def estado(self):
		print(">Marca: ", self.marca, "\n>Modelo: ", self.modelo, "\n>Arranca: ", self.arranca, "\n>Acelera:", self.acelera, "\n>Frena: ", self.frena)
