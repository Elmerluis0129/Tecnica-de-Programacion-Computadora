def sum_of_three(a=1,b=2,c=3): # a,b,c are called parameters
    d=a+b+c
    print("sum: ", d)
    
x,y,z=10,20,30
                            #x y z are arguments
sum_of_three(x,y,z)         #all variables
sum_of_three(x,y)           #Literal + variables
sum_of_three(x)             #all Literals
sum_of_three()
print()

#Another example:

def intro (age,name):
    print("Your name is ", name, " and you are ",age, " years old\n")


s= input("Enter your name: ")
a= input("Enter your age: ")
intro(a,s)

#Another example:
#Keywords arguments work here we can write any argument in any order providing name the argument. eg

def interest(prin=20000, time=1, rate=10.0):
    amt=(prin*time*rate)/100
    return amt

print(interest(rate=2, prin=20100, time=12)) #Here we change the order of interest parameters
print(interest(time=1,rate=2)) #Here we change the order of interest parameters
print(interest(time=12)) #Here we change the order of interest parameters

#This is the way for specifying names for the values is known as keyword arguments.
