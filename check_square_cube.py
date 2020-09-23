def prefect_cube(x):
    cube = 0
    for i in range(x+1):
        cube = i**3
        if cube == x:
            return True
        elif cube > x:
            return False

def prefect_square(y):
    sqr = 0
    for i in range(y+1):
        sqr = i**2
        if sqr == y:
            return True
        elif sqr > y:
            return False

def check_square_cube(a,b):
    if prefect_square(a) == prefect_cube(b):
        return True
    else:
        return False

print(check_square_cube(4,8))