print("No. 1:")
import random #This is an easier way than the form below, to create a random number from 0 to 1
r=random.random()
print(round(r,2), "\n")

print("No. 2:")
from random import * 
for i in range(5): #Here, i created like a bucle, but, the difference is that whit this form, is easier than the another form (while)
    r=random()
    print(round(r), "\t\t", r) #Here, 'round' means that variable 'r' only can have the decimal numbers that i want, in this case, is zero decimals


