#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize #Sirve para la manipulación de formularios, historiales, cokies, proxies. Documentación: (https://mechanize.readthedocs.io/en/latest/)
import argparse #Sirve para obtener algún dato que el usuario nos introduzca.
from bs4 import BeautifulSoup #Sirve para ir limpiando la respuesta que nos dé el programa.

varia = argparse.ArgumentParser() #Aquí creamos un objeto de la clase de argparse en nuestra variable.
varia.add_argument("-s", "--search", help = "Opción a buscar") #Aquí añadimos argumentos a nuestra variable, los que yo desee agregarle.
varia = varia.parse_args() #Aquí especificamos que ya no vamos agregar más argumentos a nuestra variable.

def main():
	if varia.search:
		sea = mechanize.Browser() #Aquí creamos un objeto del navegador en esta variable (sea).
		sea.set_handle_robots(False) #Aquí le damos seguimiento para que no dé error.
		sea.set_handle_equiv(False) #Aquí le damos seguimiento para que no dé error.
		sea.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0')]
		sea.open("https://www.google.com") #Aquí abrimos el sitio que ingresamos, en este caso, Google.com
		#for n in sea.forms(): #Aquí buscamos el formulario, una vez encontrado, entonces procedemos a quitar el for.
			#print(n)
		sea.select_form(nr = 0)
		sea['q'] = varia.search #Aquí tenemos que poner la letra que contiene los datos, en este caso es la "q" y luego se iguala con lo que el usuario quiere que busque.
		sea.submit() #Aquí envíamos esos datos.
		n = BeautifulSoup(sea.response().read(), 'html5lib') #Aquí imprimimos la respuesta, para ver que es lo que nos trae.
		for link in n.find_all('a'): #Aquí recorremos en busca de links de otros sitios web.
			u = link.get('href') #Aquí ya vamos eliminando las etiquetas de href.
			u = u.replace('/url?q=', '') #Aquí vamos remplazando la etiqueta /url?q= , por nada para así ir limpiando poco a poco.
			print(u)
	else:
		print("Palabra a buscar: ")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()