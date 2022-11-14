#!/usr/bin/env python
#_*_ coding: utf8 _*_

from Wappalyzer import WebPage, Wappalyzer #Wappalyzer sirve para la detencción de tecnologías presentes en un sitio web. Documentación: (https://www.wappalyzer.com/technologies)
import argparse

buscar = argparse.ArgumentParser()
buscar.add_argument('-t', '--target', help = ("Escribe la url del sitio web"))
buscar = buscar.parse_args()

def main():
	wap = Wappalyzer.latest() #Aquí construimos un objeto de wappalyzer.
	try:
		web = WebPage.new_from_url(input("Introduce la url:\n> ")) #Aquí le pedimos al usuario el sitio web al que nos conectaremos.
		tecno = wap.analyze(web) #Aquí analizamos la respuesta del sitio web.
		for t in tecno:
			print(f"Tecnología detectada: {t}")
	except:
		print("Ha ocurrido un error!")

		
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo...")
		exit()