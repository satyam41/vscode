# There are two types of loop in Python: for loop and while loop.

# for loop.
"""
Uses of for loop: use for terminate the program at given range.
Range function in for loop is take atleast one argument.
range(n) it gives output n-1.

for example: 
    if you give n = 10, the code is terminate n-1 = 10 - 1 = 9 times."""

# if you wants to give more than one argument in range function you can give to the range function.
# for example:
for i in range(1,11): # here range(1,11) means range(start, stop).
        # this mean the conting is start with 1.
        print(i)
    
# Output
1
2
3
4
5
6
7
8
9
10


"""
for i in range(11):
    print(i)
"""
# Output
0
1
1
2
3
5
8
9
10

"""first = 0
second = 1
print(first)
print(second)
n = int(input("Enter how many records you want??"))
for i in range(6):
    third = first + second
    print(third)
    first, second = second, third"""

"""for i in range(1,11):
    print("Square of number", i, end = ' ')
    print("is", i**2)"""

# while loop.

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# 
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

"""
for <variable> range(n, n-1):
    <statement>
    .
    .
"""

# for i in range(1,1001):
#     print(i)

"""
while <condition>:
    <statement>
    .
    .
"""

# a = 0
# while a<=50:
#     print(a)
#     a+=2


for i in range(1,11):
    print("Square of number", i, end = ' ')
    print("is", i**2)