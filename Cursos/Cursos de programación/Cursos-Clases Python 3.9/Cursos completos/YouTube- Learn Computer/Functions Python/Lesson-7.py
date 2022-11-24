x=10 #global accesible throughtout the program
def abc():
    global x # Here we created a new global variable.
    x=20 # Now x is global, means changes in global variable.
    print("x in abc() = ", x)
    
def efg():
    x=12 # x is local in efg
    print("x in efg() = ", x)


abc()
efg()
print("x in main = ",x)
