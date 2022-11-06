#!/usr/bin/env python
#_*_ coding: utf8 _*_

import dns.resolver # Sirve para recolectar información
from os import path 

def main():
	if path.exists('subdominios.txt'): # Sirve para comprobar si el archivo subdominios.txt existe en la ubicacion que estamos
		wordlist = open('subdominios.txt', 'r') # Abre el archivo que confirmamos que existe, en modo lectura
		wordlist = wordlist.read().split('\n') # Lo lee y lo separa con un salto de linea
		lista = []
		for s in wordlist:
			try:
				a = dns.resolver.resolve(f'{s}.google.com','A')
				lista.append(f'{s}.google.com')
			except:
				pass
		if len(lista) > 0:
			print(f"\n\nTiene aproximadamente: {len(lista)} subdominio/s\n")
			num = 1
			for e in lista:
				print(f"{num}.-", e)
				num += 1
		else:
			print("No se encontraron subdominios")
	else:
		print("No existe el archivo")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()