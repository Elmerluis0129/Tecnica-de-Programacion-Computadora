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

plt.plot(x,y,"o--r", ms = 10, mec = "k", mfc = "r") # Create grafic with the cordinates given in x2 & y2, also recive parameters to format the grafic.
plt.show() # It works for show on screen teh grafic as 'print' the python's function. But this one works with grafic.

# ms = marker size, works for marker sizes.
# mec = marker edge color, works for coloring the markers borders.
# mfc = marker face color, works for filling the markers with a color.