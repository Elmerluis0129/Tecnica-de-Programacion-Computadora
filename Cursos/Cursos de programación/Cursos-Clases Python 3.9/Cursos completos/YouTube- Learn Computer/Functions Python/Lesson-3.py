print("Example 1\n")
def sum(x,y): #Here we make a list, containing 'x' and 'y'.
    return x+y #Here we return the sum of these variables which are asked for value below.


a=int(input("Enter No 1: ")) #Value No 1, to assign that value to the 'a' variable.
b=int(input("Enter No 2: ")) #Value No 2, to assign that value to the 'b' variable.
c=sum(a,b) #Here we call the 'sum' function, so that it runs with the variables 'a' and 'b'.

print("Sum of ",a," + ",b," is: ", c, "\n") #Here we output the sum of both variables, nesting strings.

#Another way to do this would be as follows:

print("Example 2\n")
def sum(x,y): #Here we make a list, containing 'x' and 'y'.
    z=x+y     #Here we assign to the variable 'z' the value of the sum of 'x' + 'y'
    print("Sum of ",x," + ",y," is: ", z) #Here we output the sum of both variables, nesting strings.

a=int(input("Enter No 1: ")) #Value No 1, to assign that value to the 'a' variable.
b=int(input("Enter No 2: ")) #Value No 2, to assign that value to the 'b' variable.
sum(a,b) #Here we call the 'sum' function, so that it runs with the variables 'a' and 'b'.

