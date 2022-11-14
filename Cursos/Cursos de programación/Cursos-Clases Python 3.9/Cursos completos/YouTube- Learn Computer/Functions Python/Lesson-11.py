#Using randint and randrange() or range()

print("randint.")
from random import *
i=0
for i in range(9):
    i+=1
    r=randint(1,10) #This means, I create the random numbers I want between the numbers I want as well. Example: A random number from 1 to 10
    print(i,end=".- ")
    print(r)
print()    


print("randrange or range.")
i=0
for i in range(9):
    r=randrange(1,10,8)  #The parameter three means, that you can only create random numbers if they have between them a difference of the amount that parameter three indicates
    print(i,end=".- ")    #Example: randrange(1,10,8) only can create the numbers one and nine
    print(r)
print()

#Diference between randint and randrange is that in randint(1,10) include the two variables, and the randrange(1,10) only include one variable to the hour of print
#Example: randint(1,10) this print random numbers from one to ten, and randrange(1,10) only print random numbers from one to nine.
    
