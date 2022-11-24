from Paquetes.Vehiculos.MiProyectoVehiculos import *


#CAMION
if eleccion == 1:
	class camion(Vehiculo):
		def carga(self, x):
			carga = x
			if carga:
				print("El camion está cargado")

	a = camion("Yamaha", 2020)
	a.carga(True)
	a.arranco(True)


#AUTO FAMILIAR
elif eleccion == 2:
	class autoFamiliar(Vehiculo):
		def aireCarro(self, n):
			prenderAire = n
			if prenderAire:
				PotenAire = int(input("""Encendiendo aire. \n¿Qué potencia deseas en el aire? \nMenú Potencia:\n1 - 2 - 3\n> """))
				if PotenAire   == 1: 
					print("Aire encendido con una potencia de 1")
				elif PotenAire == 2: 
					print("Aire encendido con una potencia de 2")
				elif PotenAire == 3: 
					print("Aire encendido con una potencia de 3")
				else: 
					print("Solo tienes una escala del 1 al 3")
			elif not prenderAire:
				print("Aire apagado.")

			z = autoFamiliar("Yamaha", 2010)
			z.arrancoAutoFamiliar(True)

		def arrancoAutoFamiliar(self, x):
			self.arranco = x
			self.velocidadA = 20
			if self.aireCarro:
				print("Arrancando el " + usando), print("Velocidad actual: ", self.velocidad1)
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
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n  3.-Detenerte por completo\n> "))
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
			if self.arrancoHelicoptero: 
				print("Arrancando el " + usando)
				print("Velocidad actual: ", self.velocidad1)
				self.velocidadA = 50
			
			m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
			if m == 1 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif m == 1 and self.velocidadA == 100: 
				self.aceleroHeli2()
			elif m == 2: 
				deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))

			if deteniendo == 1: 
				self.frenoHeli()
			elif deteniendo == 2: 
				print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
				self.velocidadA = 50

			q = int(input("¿Qué deseas hacer? \n1.- Mantener la velocidad \n2.- Frenar, bajar, apagar y desmontarse\n> "))
			if q == 1: 
				print("De acuerdo, velocidad actual: ", self.velocidad1, "km/h")


			qu = int(input("Menu de opciones: \n0.-Acelerar \n1.-Frenar, bajar, apagar y desmontarse\n> "))
			if qu == 0 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif qu == 0 and self.velocidadA == 100:
			    self.aceleroHeli2()
			elif qu == 1: 

				print("Frenando, bajando, apagando y desmontandose del helicoptero"), exit()
			elif q == 2:
			    print("Frenando, bajando, apagando y desmontandose del helicoptero"), exit()
			r = int(input("¿Qué deseas hacer? \n1.-Acelerar el helicoptero  \n2.-Reducir la velocidad del helicoptero\n3.-Detenerte por completo y bajar helicoptero\n> "))
			if r == 1: 
				self.aceleroHelicoptero()
			elif r == 2 and self.velocidadA == 200: 
				self.reduciendoHeli3()
			elif r == 2 and self.velocidadA == 100: 
				self.reduciendoHeli2()

			elif r == 2 and self.velocidadA == 50: 
				self.reduciendoHeli1()
			elif r == 3: 
				self.frenoHeli()
			else: 
				print("Esa opción no está en el menú")

		def arrancoHeli1(self):
			print("Arrancando...")
			print("Velocidad actual: ", self.velocidad1)
			self.velocidadA = 20
			m = int(input("¿Deseas ir más rápido? 1.-Sí / 2.-No\n> "))
			if m == 1 and self.velocidadA == 20: 
				self.aceleroHeli1()
			elif m == 1 and self.velocidadA == 40: 
				self.aceleroHeli2()
			elif m == 2: 
				deteniendo = int(input("¿Deseas detenerte? 1.-Sí / 2.-No\n> "))


			if deteniendo == 1: 
				self.frenoHeli()
			while deteniendo == 2:
				print("De acuerdo\nVelocidad actual: ", self.velocidad1, "km/h\n ")
				self.velocidadA = 20
				r = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
				if r == 1: 
					self.aceleroHeli()

				elif r == 2 and self.velocidadA == 70: 
					self.reduciendoHeli3()
				elif r == 2 and self.velocidadA == 40: 
					self.reduciendoHeli2()
				elif r == 2 and self.velocidadA == 20: 
					self.reduciendoHeli1()
				elif r == 3: 
					self.frenoHeli()
				else: 
					print("Esa opción no está en el menú")

	#Aceleracion
		def aceleroHeli(self):
			print("""Acelerando...\nVelocidad actual: """, (self.velocidad1) , """km/h\n""")
			self.velocidadA = 50
			l = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
			if l == 1 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif l == 1 and self.velocidadA == 100: 
				self.aceleroHeli2()
			elif l == 2 and self.velocidadA == 200: 
				self.reduciendoHeli3()
			elif l == 2 and self.velocidadA == 100: 
				self.reduciendoHeli2()
			elif l == 2 and self.velocidadA == 50:
			 self.reduciendoHeli1()
			elif l == 3: 
				self.frenoHeli()
			elif l == 3: 
				self.frenoHeli()
			else: 
				print("Esa opción no está en el menú")

		def aceleroHeli1(self):
			print("""Acelerando...\nVelocidad actual: """, (self.velocidad2) , """km/h\n""")
			self.velocidadA = 100
			a = int(input("""¿Qué deseas hacer? \n1.-Acelerar \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> """))
			if a == 1 and self.velocidadA == 100: 
				self.aceleroHeli2()
			elif a == 1 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif a == 2 and self.velocidadA == 200: 
				self.reduciendoHeli3()
			elif a == 2 and self.velocidadA == 100: 
				self.reduciendoHeli2()
			elif a == 2 and self.velocidadA == 50: 
				self.reduciendoHeli1()
			elif a == 3: 
				self.frenoHeli()

			else: 
				print("Esa opción no está en el menú")

		def aceleroHeli2(self):
			print("""Acelerando...\nVelocidad máxima alcanzada: """, (self.velocidad3) , """km/h\n""")
			self.velocidadA = 200
			b = int(input("""¿Qué deseas hacer? \n1.-Reducir la velocidad \n2.-Detenerte por completo\n> """))
			if b == 1 and self.velocidadA == 200: 
				self.reduciendoHeli3()
			elif b == 1 and self.velocidadA == 100: 
				self.reduciendoHeli2()
			elif b == 1 and self.velocidadA == 50: 
				self.reduciendoHeli1()
			elif b == 2: 
				self.frenoHeli() 
			else: 
				print("Esa opción no está en el menú")

	#Reduccion de velocidad
		def reduciendoHeli1(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce1 + 30) , "km/h\n")
			self.velocidadA = 40
			if self.velocidadA == 140: 
				n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			elif self.velocidadA <= 55: 
				n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Detenerte por completo\n> "))
			if n == 1: 
				self.aceleroHeli()
			elif n == 2: 
				self.frenoHeli()

			else: 
				print("Esa opción no está en el menú")

		def reduciendoHeli2(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce2 + 50) , "km/h\n")
			self.velocidadA = 50
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if n == 1 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif n == 1 and self.velocidadA == 100: 
				self.aceleroHeli2()
			elif n == 2 and self.velocidadA >= 200: 
				self.reduciendoHeli3()
			elif n == 2: 
				self.reduciendoHeli1()
			elif n == 3: 
				self.frenoHeli()
			else: 
				print("Esa opción no está en el menú")

		def reduciendoHeli3(self):
			print("De acuerdo\n Reduciendo...\n Velocidad actual:  ", (self.reduce3 + 100) , "km/h\n")
			self.velocidadA = 100
			n = int(input("¿Qué deseas hacer? \n1.-Acelerar  \n2.-Reducir la velocidad\n3.-Detenerte por completo\n> "))
			if n == 1 and self.velocidadA == 50: 
				self.aceleroHeli1()
			elif n == 1 and self.velocidadA == 100: 
				self.aceleroHeli2()
			elif n == 2: 
				self.reduciendoHeli1()

			elif n == 3: 
				self.frenoHeli()
			else:
			    print("Esa opción no está en el menú")

	#Freno
		def frenoHeli(self):
			print("""De acuerdo\n Frenando...\n Velocidad actual:""", (self.velocidadA - self.velocidadA), """km/h\n""")
			d = int(input("""¿Qué deseas hacer? \n1.-Bajar, apagar, desmontarse \n2.-Arrancar\n> """))
			if d == 1: 
				self.apagandoHeli()
			elif d == 2: 
				self.arrancoHeli1()
			else: 
				print("Esa opción no está en el menú")
	#Apagado
		def apagandoHeli(self):
			print("De acuerdo\n Bajando, apagando y desmontandose del helicoptero...") 
			exit()

			
		def subiendo(self, m):
			subiendo = m
			if subiendo:
				FuncionesHeli = int(input("Helicoptero encendido. \nMenú de controles: \n1.- Subir \n2.- Apagar \n> "))

				if FuncionesHeli == 1: 
					print("Subiendo Helicoptero")
				FuncionesHeli2 = int(input("¿Deseas acelerar el helicoptero? \n1.- Si \n2.- No \n> "))
				if FuncionesHeli2 == 1: 
					self.arrancoHelicoptero(True)
				elif FuncionesHeli2 == 2:
						FuncionesHeli3 = int(input("Menú de opciones: \n1.- Bajar, apagar y desmontarse \n2.- Acelerar \n> "))
						if FuncionesHeli3 == 1: 
							print("Bajando, apagando y desmontandose del helicoptero.")
							exit()
						elif FuncionesHeli3 == 2:
							self.arrancoHelicoptero(True)						
				elif FuncionesHeli == 2:
				    print("Apagando Helicoptero") 
				FuncionesHeli4 = int(input("Menú de opciones: \n1.- Volver a encender y subir helicoptero \n2.- Desmontarse del helicoptero \n> "))
				if FuncionesHeli4 == 1: 
					print("Encendiendo y subiendo helicoptero")
				FuncionesSubiendoHeli = int(input("Menú de opciones: \n1.- Arrancar helicoptero \n2.- Apagar y desmontarse del helicoptero \n> "))
				if FuncionesSubiendoHeli == 1: 
					self.arrancoHelicoptero(True)
				elif FuncionesSubiendoHeli == 2: 
					print("Apagando y desmontandose del helicoptero"), exit()

				elif FuncionesHeli4 == 2: 
					print("Desmontandose del helicoptero")
					exit()

			elif not subiendo: 
				op = int(input("Helicoptero apagado. \nMenú de opciones: \n1.- Desmontarse \n2.- encender \n> "))
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
		