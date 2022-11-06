import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad   = edad
		print("Se ha creado una persona nueva con el nombre de " + self.nombre)

	def __str__(self): #Aqui sirve para convertir en string la informacion del objeto
		return (f"\nNombre:{self.nombre}\n---------------\nGenero:{self.genero}\n---------------\nEdad:{self.edad}\n")

class ListaPersonas:
	personas = []

	def __init__(self):
		listaDePersonas = open("fichero_externo", "ab+") #Aqui creamos un fichero y lo creamos para agregarle informacion binaria (ab+)
		listaDePersonas.seek(0) #Desplazamos el cursos a la posicion 0

		try:
			self.personas = pickle.load(listaDePersonas)
			print(f"Se cargaron {len(self.personas)} personas de el fichero externo")

		except:
			print("El fichero está vacío!!")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas = open("fichero_externo", "wb") #Abrimo el fichero externo en modo escritura binaria
		pickle.dump(self.personas, listaDePersonas) #Volcamos las variables personas, y listaDePersonas
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La información de el fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)		


miLista = ListaPersonas()
persona = Persona("Maria", "Femenino", 18)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
