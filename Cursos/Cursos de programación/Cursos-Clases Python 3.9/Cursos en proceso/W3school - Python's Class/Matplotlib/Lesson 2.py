# Learningn matplotlib Pyplot. #Lesson 2.

import matplotlib.pyplot as plt
import numpy as np

"""
With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
With Pyplot, you can use the title() function to set a title for the plot.
With Pyplot, you can use the grid() function to add grid lines to the plot.
"""

# Letter Type, Size, color.
font1 = {'family':'serif','color':'blue','size':20} # 1
font2 = {'family':'serif','color':'darkred','size':20} # 2 
font3 = {'family':'serif','color':'k','size':15} # 3
font4 = {'family':'serif','color':'green','size':17} # 3

plt.grid() # Has the same properties as the plot one. (color, linestyle, linewidth)
plt.xlabel("Luis", fontdict = font1)
plt.ylabel("Elmer", fontdict = font2)

x = np.array([0,30,15,0]) # Positions on x.
y = np.array([0,0,20,0]) # Positions on y.

x2 = np.array([0,15,7.5,0]) # Positions on x2
y2 = np.array([0,0,10,0]) # Positions on y2.

x3 = np.array([30,15,22.5,30]) # Positions on x3.
y3 = np.array([0,0,10,0]) # Positions on y3.

x4 = np.array([15,7.5,15,22.5, 15]) # Positions on x4.
y4 = np.array([20,10,0,10, 20]) # Positions on y4.


"""
Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.

linewidth can be written as lw.

dotted can be written as :.

dashed can be written as --.

"""
# 2 row, 2 columns, first plot (subplot properties)
plt.subplot(2,2,1) 
plt.plot(x,y,"*--c", ms = 15, mec = "k", mfc = "m", linestyle = '--', linewidth = 5) # Create grafic with the cordinates given in x & y, also recive parameters to format the grafic.
plt.title("Elmer", fontdict=font3)
plt.xlabel("X-axis", fontdict=font1)
plt.ylabel("Y-axis", fontdict=font2)

# 2 row, 2 columns, second plot (subplot properties)
plt.subplot(2,2,2)
plt.plot(x2,y2,"--y", linestyle = '--', linewidth = 3) # Create grafic with the cordinates given in x2 & y2, also recive parameters to format the grafic.
plt.subplot(2,2,2)
plt.plot(x3,y3,"--r", linestyle = '--', linewidth = 3) # Create grafic with the cordinates given in x3 & y3, also recive parameters to format the grafic.
plt.subplot(2,2,2)
plt.plot(x4,y4,"--b", linestyle = '--', linewidth = 3) # Create grafic with the cordinates given in x4 & y4, also recive parameters to format the grafic.
plt.title("Luis",fontdict=font3)
plt.xlabel("X-axis", fontdict=font1)
plt.ylabel("Y-axis", fontdict=font2)

# PIE CHART
# 2 row, 2 columns, third plot (subplot properties)
plt.subplot(2,2,3)
y = np.array([35, 25, 25, 15]) # Porcent of each one of them.
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels) # Here will create the pie chart.
plt.legend(title = "Four Fruits:")  # List of explanation for each wedge with title.


# Histogram plot
# 2 row, 2 columns, fourth plot (subplot properties)
plt.subplot(2,2,4)
x = np.random.normal(170, 10, 250) # This will generate a random result
plt.hist(x) # The hist() function will read the array and produce a histogram

plt.suptitle("Learning with w3school / Matplotlib.Pyplot", fontdict = font4)
plt.show() # It works for show on screen teh grafic as 'print' the python's function. But this one works with grafic.