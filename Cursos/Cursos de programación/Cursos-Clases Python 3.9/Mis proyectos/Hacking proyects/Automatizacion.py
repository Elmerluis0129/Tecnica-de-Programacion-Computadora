import os
from email.message import EmailMessage
import ssl
import smtplib

#Contraseña de: elmersainthilarerojo@gmail.com = oduwmzxzhyexhdih
#Email y contraseña de quien quiere mandar el correo.
email_emisor = 'elmersainthilarerojo@gmail.com'
email_contrasena = 'oduwmzxzhyexhdih'
#Email de quien va recibir el correo.
email_receptor = 'es21-1354@unphu.edu.do'

asunto = 'Automatizando con python'
cuerpo = """

He automatizado python con gmail, para mandar correos
sin tener que mandarlos directamente por la plataforma de 
Google Gmail, solo tengo que abrir mi programa y escribir 
todos los datos necesarios y listo, justo como lo hice 
con este correo.

¡Funcionó!

"""

em = EmailMessage()

em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
	smtp.login(email_emisor, email_contrasena)
	smtp.sendmail(email_emisor, email_receptor, em.as_string())

