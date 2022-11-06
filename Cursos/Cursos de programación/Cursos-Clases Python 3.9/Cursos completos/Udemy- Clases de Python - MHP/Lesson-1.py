#@classmethod
#@staticmethod
#@property

class prueba1(object):
	def __init__(self,radio):
		self.radio = radio

	@classmethod #Nos ayuda a usar una función sin que antes ésta sea atribuida a un objeto.
	def saludo(cls,nombre):
		print(f"Hola, {str(nombre)}")

	@staticmethod #Sirve para ejecutar una función sin argumentos alguno.
	def saludo_static():
		print("Bienvenidos")

	@property #Sirve para modificar un método para que sea un atributo o propiedad.
	def area_circulo(self):
		return 3.1416 * (self.radio **2)
	
def main():
	#nombre = input("Nombre: ")
	#prueba1.saludo(nombre)
	c = prueba1(5)
	area = c.area_circulo
	print(round(area, 2))

if __name__ == "__main__":
	main()