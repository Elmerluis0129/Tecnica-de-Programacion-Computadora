class Auto():
	def __init__(self):
		self.__largo            = 250
		self.__ancho            = 100
		self.__ruedas           = 4
		self.__puertas          = 4
		self.AutoPrendido       = False
		self.modoAutomatico     = False 
		self.frenando           = True

	def estado(self):
		if self.AutoPrendido and self.modoAutomatico:
			print("""Estado> \nAutomovil: Encendido\nModo automatico: Encendido\n""")
		elif self.AutoPrendido and self.modoAutomatico == False:
			print("""Estado> Automovil: Encendido\n""")
		elif self.AutoPrendido == False:
			print("""Estado> Automovil: Apagado""")


	def enciende(self, vamonos): 
		self.frenando = vamonos
		if self.frenando:
			preguntar = int(input("""¿Deseas encender el automovil?\n1- Sí\n2- No\n>"""))
		if preguntar == 1:
			print("Encendiendo automovil...\n")
			self.AutoPrendido = True
			self.estado()
			modoAutomatico = int(input("""\n¿Deseas encender el modo automatico?\n1- Sí\n2- No\n>""")) 
			if modoAutomatico == 1:
				self.modoAutomatico = True
				self.estado()
			elif modoAutomatico == 2:
				self.estado()
			else: 
				print("La opción no está en el menu")
				
		elif preguntar == 2:
			self.estado()
		else:
			print("Esa opción no está en el menú.")

a = Auto()
print(a.enciende(True))
