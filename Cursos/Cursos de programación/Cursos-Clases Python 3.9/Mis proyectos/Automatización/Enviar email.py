import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

#elmersainthilarerojo@gmail.com = oduwmzxzhyexhdih
#elmerluissainthilarerojo@gmail.com = ncuuleaqdjaxccaf
#Email y contraseña de quien quiere mandar el correo.
email_emisor = 'elmersainthilarerojo@gmail.com'
email_contrasena = 'oduwmzxzhyexhdih'
#Email de quien va recibir el correo.
email_receptor = 'elmerluissainthilarerojo@gmail.com'

asunto = 'Anti-Aus habbo'
cuerpo = """

¡Funcionó!

"""

em = EmailMessage()

em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)

#Adjuntar archivo:
#Recuerda llevar la imagen a la misma ubicacion que el programa: C:\Users\elmer\OneDrive\Escritorio\Elmer\Cursos\Cursos de programación\Cursos-Clases Python 3.9\Mis proyectos\Automatización
#Solo cambiaría el nombre de la imagen, el rb queda igual, lo demás también.
with open('Anti-Aus Automático.jpg', 'rb') as file:
	file_data = file.read()
	file_tipo = imghdr.what(file.name)
	file_nombre = file.name
em.add_attachment(file_data, filename=file_nombre, subtype=file_tipo, maintype='image')


contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
	smtp.login(email_emisor, email_contrasena)
	smtp.sendmail(email_emisor, email_receptor, em.as_string())

