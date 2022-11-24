#El programa se ejecuta: 1,3,4,1,2,5,6.

def ssm(x,y): #Line 1
    return x+y, x*y, x-y #Line 2

a=int(input("Enter No 1: ")) #Line 3 
b=int(input("Enter No 2: ")) #Line 4
c=ssm(a,b) # 'c' is tuple ... #Line 5
print("Addition, multiplication and subration of ",a, " and",b, " is",c) #Line 6
