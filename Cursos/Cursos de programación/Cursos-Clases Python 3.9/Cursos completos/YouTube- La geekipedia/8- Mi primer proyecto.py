#Sistema para calcular el promedio de un alumno

print("Sistema para calcular el promedio de un alumno.");

nombre = input("Para comenzar, ¿cuál es tu nombre?: ");

matematicas = float(input(nombre + ", ¿cuál es tu calificación en matematicas?: "));
quimica = float(input(nombre + ", ¿cuál es tu calificación en química?: "));
biologia = float(input(nombre + ", ¿cuál es tu calificación en biología?: "));

promedio =(matematicas + quimica + biologia)/3;


if promedio >= 6 and promedio <= 10:
    print('Felicidades ' + nombre + ', "aprobaste" con un promedio de: ', round(promedio, 1));
else:
    if promedio < 6:
        print('Lo siento ' + nombre + ', "reprobaste" con un promedio de: ', round(promedio, 1));
    else:
        if promedio > 10:
            print(nombre + ' recuerda que el programa de calificación, se valora con un porcentaje del 1 al 10, haz el favor e intentalo de nuevo');
            
print('Fin.');
