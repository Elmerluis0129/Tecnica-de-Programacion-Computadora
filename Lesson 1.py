# Learningn matplotlib Pyplot. #Lesson 1.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6,7,19,12,15.4]) # Posiciones en x.
y = np.array([0,10,12,13,19.8,20]) # Posiciones en y.

"""
fmt / " "

*------------------*
| Marker Reference |
*------------------*

Marker	|Description
'o'	    |  Circle	
'*'	    |  Star	
'.'	    |  Point	
','	    |  Pixel	
'x'	    |  X	
'X'	    |  X (filled)	
'+'	    |  Plus	
'P'	    |  Plus (filled)	
's'	    |  Square	
'D'	    |  Diamond	
'd'	    |  Diamond (thin)	
'p'	    |  Pentagon	
'H'	    |  Hexagon	
'h'	    |  Hexagon	
'v'	    |  Triangle Down	
'^'	    |  Triangle Up	
'<'	    |  Triangle Left	
'>'	    |  Triangle Right	
'1'	    |  Tri Down	
'2'	    |  Tri Up	
'3'	    |  Tri Left	
'4'	    |  Tri Right	
'|'	    |  Vline	
'_'	    |  Hline

*--------------*
|Line Reference|
*--------------*

Line Syntax	| Description
'-'	        | Solid line	
':'	        | Dotted line	
'--'	    | Dashed line	
'-.'	    | Dashed/dotted line

*---------------*
|Color Reference|
*---------------*

Color Syntax | Description
'r'	         |    Red	
'g'	         |    Green	
'b'	         |    Blue	
'c'	         |    Cyan	
'm'	         |    Magenta	
'y'	         |    Yellow	
'k'	         |    Black	
'w'	         |    White

"""

#Syntax, marker reference + line reference + color reference

#Example:

plt.plot(x,y,"o--r", ms = 10, mec = "k", mfc = "r") # Crea la grafica segun las cordenadas dadas en x & y, tambien recive parametros para darle formato al grafico.
plt.show() # Sirve para mostrar en pantalla lo que se especifica arriba, es como el print en python.

# ms = marker size, sirve para darle tamño a los markadores.
# mec = marker edge color, sirve para colorear los bordes de los marcadores.
# mfc = marker face color, sirve para colorear los fondos de los marcadores.