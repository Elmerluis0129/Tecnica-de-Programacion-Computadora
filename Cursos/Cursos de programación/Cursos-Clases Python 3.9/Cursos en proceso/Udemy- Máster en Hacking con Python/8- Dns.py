#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver # Sirve para recolectar informacion

def main():
	consulta = ['A', 'MX']
	for x in consulta:
		try:
			b = dns.resolver.resolve("google.com", x) # Sirve para hacer consultas, en este caso en google, y recibe como parametros 2 valores, uno es el objetivo  el otro es el tipo de busqueda que se va hacer (dns)
			for x in b:
 				print("> ", x)
		except:
			print("No pude obtener la consulta")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()