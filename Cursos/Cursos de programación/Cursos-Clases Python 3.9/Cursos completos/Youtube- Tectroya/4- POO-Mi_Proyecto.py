#Mi proyecto, basado en mis conocimientos básicos... (eN CONSTRUCION)
# Elmer Luis Saint-Hilare Rojo
# Sistema de vehículos

"""
Esto es un sistema que simula vehículos. Básicamente este sistema tiene 4 opciones de vehículos, los cuales según vayas selecionando tienen sus distintas funcionalidades y todo fue realizado con POO. Ya que fue con el propósito de poner en práctica mis conocimientos
relacionados con la programación orientada a objetos con python.
"""
eleccion = int(input("""
¿En qué vehiculo vas a salir?

*------------------*
|1.- Camion        |
|2.- Auto familiar |
|3.- Helicoptero   |
|4.- Moto electrica|
*------------------*

> """))

while True:
	if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4:
		break
	else:
		print("\nOpción no brindada anteriormente.")
		print("Vuelve a intentarlo. \n")
		eleccion = int(input("""
¿En qué vehiculo vas a salir?

*------------------*
|1.- Camion        |
|2.- Auto familiar |
|3.- Helicoptero   |
|4.- Moto electrica|
*------------------*

> """))
		

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
		self.velocidadG = False
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
		if self.arranco and eleccion != 4 and eleccion : print("Montandose, encendiendo y arrancando el " + usando), print("Velocidad actual: ", self.velocidad1)
		elif self.arranco and eleccion == 4: print("Montandose, encendiendo y arrancando la " + usando)
		self.velocidadG = 20
		m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
		if m == 1 and self.velocidadG == 20: self.acelero1()
		elif m == 1 and self.velocidadG == 40: self.acelero2()
		elif m == 2: deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
		if deteniendo == 1: self.freno()
		while deteniendo == 2: 
			print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
			self.velocidadG = 20
		r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n  3.-Detenerte por completo\n> "))
		if r == 1: self.acelero()
		elif r == 2 and self.velocidadG == 70: self.reduciendo3()
		elif r == 2 and self.velocidadG == 40: self.reduciendo2()
		elif r == 2 and self.velocidadG == 20: self.reduciendo1()
		elif r == 3: self.freno()
		else: print("Esa opción no está en el menú")

	def arranco1(self):
		print("Arrancando...")
		print("Velocidad actual: ", self.velocidad1)
		self.velocidadG = 20
		m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
		if m == 1 and self.velocidadG == 20: self.acelero1()
		elif m == 1 and self.velocidadG == 40: self.acelero2()
		elif m == 2: deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
		if deteniendo == 1: self.freno()
		while deteniendo == 2:
			print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
			self.velocidadG = 20
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if r == 1: self.acelero()
			elif r == 2 and self.velocidadG == 70: self.reduciendo3()
			elif r == 2 and self.velocidadG == 40: self.reduciendo2()
			elif r == 2 and self.velocidadG == 20: self.reduciendo1()
			elif r == 3: self.freno()
			else: print("Esa opción no está en el menú")

#Aceleracion
	def acelero(self):
		print("""Acelerando...\nVelocidad actual: """, (self.velocidad1) , """km/h\n""")
		self.velocidadG = 20
		l = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
		if l == 1 and self.velocidadG == 20: self.acelero1()
		elif l == 1 and self.velocidadG == 40: self.acelero2()
		elif l == 2 and self.velocidadG == 70: self.reduciendo3()
		elif l == 2 and self.velocidadG == 40: self.reduciendo2()
		elif l == 2 and self.velocidadG == 20: self.reduciendo1()
		elif l == 3: self.freno()
		elif l == 3: self.freno()
		else: print("Esa opción no está en el menú")

	def acelero1(self):
		print("""Acelerando...\nVelocidad actual: """, (self.velocidad2) , """km/h\n""")
		self.velocidadG = 40
		a = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
		if a == 1 and self.velocidadG == 40: self.acelero2()
		elif a == 1 and self.velocidadG == 20: self.acelero1()
		elif a == 2 and self.velocidadG == 70: self.reduciendo3()
		elif a == 2 and self.velocidadG == 40: self.reduciendo2()
		elif a == 2 and self.velocidadG == 20: self.reduciendo1()
		elif a == 3: self.freno()
		else: print("Esa opción no está en el menú")

	def acelero2(self):
		print("""Acelerando...\nVelocidad máxima alcanzada: """, (self.velocidad3) , """km/h\n""")
		self.velocidadG = 70
		b = int(input("""¿Qué deseas hacer? \n1.-Reducir la velocidad \n2.-Detenerte por completo\n> """))
		if b == 1 and self.velocidadG == 70: self.reduciendo3()
		elif b == 1 and self.velocidadG == 40: self.reduciendo2()
		elif b == 1 and self.velocidadG == 20: self.reduciendo1()
		elif b == 2: self.freno() 
		else: print("Esa opción no está en el menú")

#Reduccion de velocidad
	def reduciendo1(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce1) , "km/h\n")
		self.velocidadG = 10
		if self.velocidadG == 20: n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		elif self.velocidadG <= 15: n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Detenerte por completo\n> "))
		if n == 1: self.acelero()
		elif n == 2: self.freno()
		else: print("Esa opción no está en el menú")

	def reduciendo2(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce2) , "km/h\n")
		self.velocidadG = 20
		n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		if n == 1 and self.velocidadG == 20: self.acelero1()
		elif n == 1 and self.velocidadG == 40: self.acelero2()
		elif n == 2 and self.velocidadG >= 70: self.reduciendo3()
		elif n == 2: self.reduciendo1()
		elif n == 3: self.freno()
		else: print("Esa opción no está en el menú")

	def reduciendo3(self):
		print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce3) , "km/h\n")
		self.velocidadG = 40
		n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
		if n == 1 and self.velocidadG == 20: self.acelero1()
		elif n == 1 and self.velocidadG == 40: self.acelero2()
		elif n == 2: self.reduciendo1()
		elif n == 3: self.freno()
		else: print("Esa opción no está en el menú")

#Freno
	def freno(self):
		print("""De acuerdo\n Frenando...\n Velocidad actual:""", (self.velocidadG - self.velocidadG), """km/h\n""")
		d = int(input("""¿Qué deseas hacer? \n1.-Apagar \n2.-Arrancar\n> """))
		if d == 1: self.apagandom()
		elif d == 2: self.arranco1()
		else: print("Esa opción no está en el menú")

#Apagado
	def apagandom(self):
		f = int(input("De acuerdo\n Apagando...\n ¿Qué deseas hacer? \n1.-Encender y arrancar \n2.-Desmontarse\n> "))
		if f == 1: self.arranco1()
		elif f == 2: print("Desmontandose..."), exit()
		else: print("Esa opción no está en el menú")

#Estado del vehiculo	
	def estado(self):
		print(">Marca: ", self.marca, "\n>Modelo: ", self.modelo, "\n>Arranca: ", self.arranca, "\n>Acelera:", self.acelera, "\n>Frena: ", self.frena)
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# POLIMORFISMO.

#CAMION
if eleccion == 1:
	class camion(Vehiculo):
		def carga(self, x):
			carga = x
			if carga:
				print("El camion está cargado\n")

	a = camion("Yamaha", 2020)
	a.carga(int(input("\nPresione 1 para cargar el camión, presione 0 para no hacerlo.\n>")))
	a.arranco(True)


#AUTO FAMILIAR
elif eleccion == 2:
	class autoFamiliar(Vehiculo):
		def aireCarro(self, n):
			prenderAire = n
			if prenderAire:
				PotenAire = int(input("""Encendiendo aire. 
¿Qué potencia deseas en el aire? 
Menú Potencia:
1 - 2 - 3
> """))
				if PotenAire   == 1: print("Aire encendido con una potencia de 1")
				elif PotenAire == 2: print("Aire encendido con una potencia de 2")
				elif PotenAire == 3: print("Aire encendido con una potencia de 3")
				else: print("Solo tienes una escala del 1 al 3")
			elif not prenderAire:
				print("Aire apagado.")

			z = autoFamiliar("Yamaha", 2010)
			z.arrancoAutoFamiliar(True)

		def arrancoAutoFamiliar(self, x):
			self.arranco = x
			self.velocidadG = 20
			if self.aireCarro:
				print("Arrancando el " + usando), print("Velocidad actual: ", self.velocidad1)
			m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
			if m == 1 and self.velocidadG == 20: self.acelero1()
			elif m == 1 and self.velocidadG == 40: self.acelero2()
			elif m == 2: deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
			if deteniendo == 1: self.freno()
			while deteniendo == 2: 
				print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
				self.velocidadG = 20
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n  3.-Detenerte por completo\n> "))
			if r == 1: self.acelero()
			elif r == 2 and self.velocidadG == 70: self.reduciendo3()
			elif r == 2 and self.velocidadG == 40: self.reduciendo2()
			elif r == 2 and self.velocidadG == 20: self.reduciendo1()
			elif r == 3: self.freno()
			else: print("Esa opción no está en el menú")

	b = autoFamiliar("Hyundai", 2015)
	b.aireCarro(int(input("\n¿Deseas encender el aire? \n1.- Sí \n0.- No\n> ")))


#HELICOPTERO
elif eleccion == 3:
	class helicoptero(Vehiculo):
		def arrancoHelicoptero(self, x):
			self.arrancoHelicoptero = x
			self.velocidad1 = 50
			self.velocidad2 = 100
			self.velocidad3 = 200
			if self.arrancoHelicoptero: print("Arrancando el " + usando), print("Velocidad actual: ", self.velocidad1)
			self.velocidadG = 50
			m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
			if m == 1 and self.velocidadG == 50: self.aceleroHeli1()
			elif m == 1 and self.velocidadG == 100: self.aceleroHeli2()
			elif m == 2: deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
			if deteniendo == 1: self.frenoHeli()
			if deteniendo == 2: print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
			self.velocidadG = 50
			q = int(input("¿Qué deseas hacer? \n1.- Mantener la velocidad \n2.- Frenar, bajar, apagar y desmontarse\n> "))
			if q == 1: print("De acuerdo, velocidad actual: ", self.velocidad1, "km/h")
			qu = int(input("Menu de opciones: \n0.-Acelerar \n1.-Frenar, bajar, apagar y desmontarse\n> "))
			if qu == 0 and self.velocidadG == 50: self.aceleroHeli1()
			elif qu == 0 and self.velocidadG == 100: self.aceleroHeli2()
			elif qu == 1: print("Frenando, bajando, apagando y desmontandose del helicoptero"), exit()
			elif q == 2: print("Frenando, bajando, apagando y desmontandose del helicoptero"), exit()
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar el helicoptero  \n2.-Reducir la velocidad del helicoptero\n3.-Detenerte por completo y bajar helicoptero\n> "))
			if r == 1: self.aceleroHelicoptero()
			elif r == 2 and self.velocidadG == 200: self.reduciendoHeli3()
			elif r == 2 and self.velocidadG == 100: self.reduciendoHeli2()
			elif r == 2 and self.velocidadG == 50: self.reduciendoHeli1()
			elif r == 3: self.frenoHeli()
			else: print("Esa opción no está en el menú")

		def arrancoHeli1(self):
			print("Arrancando...")
			print("Velocidad actual: ", self.velocidad1)
			self.velocidadG = 20
			m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
			if m == 1 and self.velocidadG == 20: self.aceleroHeli1()
			elif m == 1 and self.velocidadG == 40: self.aceleroHeli2()
			elif m == 2: deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))
			if deteniendo == 1: self.frenoHeli()
			while deteniendo == 2:
				print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
				self.velocidadG = 20
				r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
				if r == 1: self.aceleroHeli()
				elif r == 2 and self.velocidadG == 70: self.reduciendoHeli3()
				elif r == 2 and self.velocidadG == 40: self.reduciendoHeli2()
				elif r == 2 and self.velocidadG == 20: self.reduciendoHeli1()
				elif r == 3: self.frenoHeli()
				else: print("Esa opción no está en el menú")

	#Aceleracion
		def aceleroHeli(self):
			print("""Acelerando...\nVelocidad actual: """, (self.velocidad1) , """km/h\n""")
			self.velocidadG = 50
			l = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
			if l == 1 and self.velocidadG == 50: self.aceleroHeli1()
			elif l == 1 and self.velocidadG == 100: self.aceleroHeli2()
			elif l == 2 and self.velocidadG == 200: self.reduciendoHeli3()
			elif l == 2 and self.velocidadG == 100: self.reduciendoHeli2()
			elif l == 2 and self.velocidadG == 50: self.reduciendoHeli1()
			elif l == 3: self.frenoHeli()
			elif l == 3: self.frenoHeli()
			else: print("Esa opción no está en el menú")

		def aceleroHeli1(self):
			print("""Acelerando...\nVelocidad actual: """, (self.velocidad2) , """km/h\n""")
			self.velocidadG = 100
			a = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
			if a == 1 and self.velocidadG == 100: self.aceleroHeli2()
			elif a == 1 and self.velocidadG == 50: self.aceleroHeli1()
			elif a == 2 and self.velocidadG == 200: self.reduciendoHeli3()
			elif a == 2 and self.velocidadG == 100: self.reduciendoHeli2()
			elif a == 2 and self.velocidadG == 50: self.reduciendoHeli1()
			elif a == 3: self.frenoHeli()
			else: print("Esa opción no está en el menú")

		def aceleroHeli2(self):
			print("""Acelerando...\nVelocidad máxima alcanzada: """, (self.velocidad3) , """km/h\n""")
			self.velocidadG = 200
			b = int(input("""¿Qué deseas hacer? \n1.-Reducir la velocidad \n2.-Detenerte por completo\n> """))
			if b == 1 and self.velocidadG == 200: self.reduciendoHeli3()
			elif b == 1 and self.velocidadG == 100: self.reduciendoHeli2()
			elif b == 1 and self.velocidadG == 50: self.reduciendoHeli1()
			elif b == 2: self.frenoHeli() 
			else: print("Esa opción no está en el menú")

	#Reduccion de velocidad
		def reduciendoHeli1(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce1 + 30) , "km/h\n")
			self.velocidadG = 40
			if self.velocidadG == 140: n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			elif self.velocidadG <= 55: n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Detenerte por completo\n> "))
			if n == 1: self.aceleroHeli()
			elif n == 2: self.frenoHeli()
			else: print("Esa opción no está en el menú")

		def reduciendoHeli2(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce2 + 50) , "km/h\n")
			self.velocidadG = 50
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if n == 1 and self.velocidadG == 50: self.aceleroHeli1()
			elif n == 1 and self.velocidadG == 100: self.aceleroHeli2()
			elif n == 2 and self.velocidadG >= 200: self.reduciendoHeli3()
			elif n == 2: self.reduciendoHeli1()
			elif n == 3: self.frenoHeli()
			else: print("Esa opción no está en el menú")

		def reduciendoHeli3(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce3 + 100) , "km/h\n")
			self.velocidadG = 100
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if n == 1 and self.velocidadG == 50: self.aceleroHeli1()
			elif n == 1 and self.velocidadG == 100: self.aceleroHeli2()
			elif n == 2: self.reduciendoHeli1()
			elif n == 3: self.frenoHeli()
			else: print("Esa opción no está en el menú")

	#Freno
		def frenoHeli(self):
			print("""De acuerdo\n Frenando...\n Velocidad actual:""", (self.velocidadG - self.velocidadG), """km/h\n""")
			d = int(input("""¿Qué deseas hacer? \n1.-Bajar, apagar, desmontarse \n2.-Arrancar\n> """))
			if d == 1: self.apagandoHeli()
			elif d == 2: self.arrancoHeli1()
			else: print("Esa opción no está en el menú")
	#Apagado
		def apagandoHeli(self):
			print("De acuerdo\n Bajando, apagando y desmontandose del helicoptero...") 
			exit()
			
		def subiendo(self, m):
			subiendo = m
			if subiendo:
				FuncionesHeli = int(input("Helicoptero encendido. \nMenú de controles: \n1.- Subir \n2.- Apagar \n> "))

				if FuncionesHeli == 1: print("Subiendo Helicoptero")
				FuncionesHeli2 = int(input("¿Deseas acelerar el helicoptero? \n1.- Si \n2.- No \n> "))
				if FuncionesHeli2 == 1: self.arrancoHelicoptero(True)
				elif FuncionesHeli2 == 2:
						FuncionesHeli3 = int(input("Menú de opciones: \n1.- Bajar, apagar y desmontarse \n2.- Acelerar \n> "))
						if FuncionesHeli3 == 1: 
							print("Bajando, apagando y desmontandose del helicoptero.")
							exit()
						elif FuncionesHeli3 == 2:
							self.arrancoHelicoptero(True)						
				elif FuncionesHeli == 2: print("Apagando Helicoptero") 
				FuncionesHeli4 = int(input("Menú de opciones: \n1.- Volver a encender y subir helicoptero \n2.- Desmontarse del helicoptero \n> "))
				if FuncionesHeli4 == 1: print("Encendiendo y subiendo helicoptero")
				FuncionesSubiendoHeli = int(input("Menú de opciones: \n1.- Arrancar helicoptero \n2.- Apagar y desmontarse del helicoptero \n> "))
				if FuncionesSubiendoHeli == 1: self.arrancoHelicoptero(True)
				elif FuncionesSubiendoHeli == 2: print("Apagando y desmontandose del helicoptero"), exit()

				elif FuncionesHeli4 == 2: print("Desmontandose del helicoptero")
				exit()

			elif not subiendo: op = int(input("Helicoptero apagado. \nMenú de opciones: \n1.- Desmontarse \n2.- encender \n> "))
			if op == 1:
					print("Desmontandose.")
					exit()
			elif op == 2:
					x = True
					self.subiendo(x)

			z = helicoptero("Mazzu", "12AB")
			z.arrancoHelicoptero(int(input("¿Quieres encender el helicoptero? \n1.- Si \n0.- No \n> ")))


	z = helicoptero("Mazzu", "12AB")
	z.subiendo(int(input("¿Quieres encender el helicoptero? \n1.- Si \n0.- No \n")))

#Moto Electrica
elif eleccion == 4:
	print("Este vehiculo esta en proceso de construcion")
	class motoElec(Vehiculo):
		pass	