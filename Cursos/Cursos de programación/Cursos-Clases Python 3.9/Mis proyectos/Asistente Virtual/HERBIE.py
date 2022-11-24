#Humanoid Experimental Robot, B-type, Integrated Electronics

import speech_recognition as sr
import pyttsx3, pywhatkit

name = "Herbie" #Nombre de la asistente
listener = sr.Recognizer() #Con esto la asistente va a reconocer.
engine = pyttsx3.init() #Creamos un objeto de tipo pyttsx3 en nuestra variable engine

voices = engine.getProperty('voices') #Aqui utilizamos la variable engine, para obtener la propiedades de voces
engine.setProperty('voice', voices[0].id) #Aqui le ponemos la voz que esta en la posicion 0 'Sabina'

def talk(text):
    engine.say(text) #Aqui para que diga todo lo que se le escriba
    engine.runAndWait() #Aqui es para que corra y espere

def listen():
    try:
        with sr.Microphone() as source: #Esto para que tome como puente nuestro microfono
            print("Escuchando...")      
            pc = listener.listen(source) #Aqui ya el microfono escucha todo lo que decimos
            rec = listener.recognize_google(pc) #Aqui le decimos que utilize los recursos de reconocimiento de voz de google y lo use desde pc
            rec = rec.lower()
            if name in rec: #Condicion
                rec = rec.replace(name, '') #Al nombre lo remplaza con nada, si se cumple la condicion        
    except:
        print("Lo siento, elmer")
    return rec

def run_herbie(): #Funcion para los comandos que se le van a integrar a herbie
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciendo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music) #Sirve para que herbie vaya a YouTube a reproducir la musica

if __name__ == '__main__':
    run_herbie()