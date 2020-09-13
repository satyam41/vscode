"""Function is mainly two types built-in function and user-define function.
Example of built-in function: print(), input(), get() etc.

creation of functions:

def <function_name>([<parameter>,<parameters2>]):
    statement1....
    [statement]....
    [return]

def = defination of that function.


def function():
    print("Hello!, I am first comment.")

#-----Main Program-----

print("Satyam krishan", function())

# Defination of function to adding two numbers.
def ADD(x,y):
    z = x+y
    return z

# Defination of function to subtracting two numbers.
def SUB(x,y):
    z = x-y
    return z

# Defination of function to multipling two numbers.
def MULT(x,y):
    z = x*y
    return z

# Defination of function to divide two numbers.
def DIV(x,y):
    z = x/y
    return z

# Defination of function to get reminder from divisior.
def REM(x,y):
    z = x%y
    return z

# Defination of function to solve power of the numbers.
def POW(x,y):
    z = x**y
    return z

# Defination of function to flore division of two numbers.
def FLOR(x,y):
    z = x//y
    return z

#-----Main Program-----

a = 10 
b = 20
c = ADD(a,b)
print("The sum of c is", c)


# Defination of Simple Interest Calculator.
def SimpleInterest(P,R,T):
    si = P*R*T/100
    return si

#-----Main Program-----

p = 1000
r = 100
t = 2
SI = SimpleInterest(p,r,t)
print("Simple Interest is", SI)

# Defination of get maximum and minimum number from list, tuple.
# Defination maximum function.
def MAX(x):
    big = x[0]
    j = 0
    for i in x:
        if (x[j]>=big):
            big = x[j]
            j = j+1
        else:
            j = j+1
    return big

# Defination minimum function.
def MIN(y):
    small = y[0]
    k = 0
    for i in y:
        if (y[k]<=small):
            small = y[k]
            k = k + 1
        else:
            k = k + 1
    return small

#-----Main Program-----
lst = [2,45,5,7,44,6,11,9,3,50]
print("Maximum number from list is", MAX(lst))
print("Minmum number from list is", MIN(lst))


# Defination of serach function.

def SEARCH(x, item):
    boolean = False
    for i in x:
        if (i == item):
            boolean = True
            break
        else:
            boolean = False
    return boolean
#-----Main Program------

lst = [2,45,5,7,44,6,11,9,3,50]
a = 77 # eval(input("Enter what you want to search??? : "))
flag = SEARCH(lst, a)
if (flag):
    print("Data Found")
else:
    print("No Data Found")

# Variable neither local scope or nor in global scope.
name = "Satyam"
def greet():
    name = "Krishna"
    print("Hello", name)

print(name)
greet()

# Some variable name in local scope as well as global scope.

def stage1():
    global tiger
    tiger = 15
    print(tiger)
tiger = 95
print(tiger)
print(tiger)
stage1()
print(tiger)
print(tiger)


def myFunc(x):
    print("\t Inside myFunc()")
    print("\t Value received in 'x' as ",x)
    x = x + 2
    print("\t Value of 'x' now changes to", x)
    print("\t Returning from myFunc()")
#----manin program----
num = 3
print("Calling myFunc() ny passing 'num' with value", num)
myFunc(num)
print("Back form myFunc(). Value of 'num' is", num)"""