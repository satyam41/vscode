"""Function are mainly two types (i).Built-in function.
                              (ii).User-define function.
(i).Built-in Function : Here we can use directly any function from any module or any python function.
(ii).User-define function : Here we can define the function our own.

CREATING OF FUNCTION :

DEFINATION OF FUNCTION 

'def <function_name>([<parameter1>,<parameter2>,.....]):
    statement1
    [statement2]
    .....
    ....
    return'

CALLING OF FUNCTION
'<function_name>([<variabe1>,<variable2>,......])'

def means : defination of function.
() : In paranthese write parameters.
[] : optional"""

"""# Defination of first function 

def func_1():
    print(f"Hello {name}")

# -----Main Program-----
name = "Satyam"
# func_1()

# Defination of add, subract, multiplie, divied, flor division, remainder, power.

def add(x,y):
    z = x+y
    return z
def sub(x,y):
    z = x-y
    return z
def mult(x,y):
    z = x*y
    return z
def div(x,y):
    z = x/y
    return z
def fld(x,y):
    z = x//y
    return z
def reim(x,y):
    z = x%y
    return z
def powe(x,y):
    z = x**y
    return z

# ------Main Program------
a = 10 
b = 20
print("The sum is", add(a,b))"""

# Defination of SEARCH function.

def SEARCH(x,item):
    boolean = False
    for i in x:
        if (i==item):
            boolean = True
            break
        else:
            boolean = False
    return boolean
# ------Main Program------
lst = [1,5,3,8,55,8]
a = 5
flag = SEARCH(lst,a)
if flag:
    print(f"{a} in list....Data Found")
else:
    print(f"{a} not in list....No Data Found")