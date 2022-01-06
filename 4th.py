# Conditions
# if, elif and else statement.

# You heard about word conditions in English. In Python the meaning of condition is same.

"""
Lets take some example to understand what is condition and why we use conditional statement in any programming language.

Example of conditional statement in real life: 
    If the hypothesis is false, the conclusion is false.

Example of conditional statement in programming language:
    If your age is greater than 18 than you can drive, if your age is less than 18 you cannot drive....
"""

# Q.Write a program to show you are eligible or not eligible for drive any car or bick and take age input from user.

# Solution:

age = int(input("Enter your age : "))
if age >= 10 and age < 18:
    print("You drive a cycle.")
elif age < 10:
    print("You can not drive any thing.")
else:
    print("You can drive cycle as well as bike, car etc.")


# Q.Write a program to print the Quotient of the any number. If denominator is 0 print a message to the user "Division by Zero is not possible"...

# Solution

a = b = c = 0
a = 100
b = 0
if b == 0:
    print("Division by zero is not possible Error! Aborting!")
else:
    c = a/b
    print("Quotient =", c)
print("Program Over!!!")

# Question of the day: Print the multiplication table of any number.