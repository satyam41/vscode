"""
choose any number
take from some one and add both the number

take the number from computer

sum of all three number

half of the number

return the same number you take from the second user

result = half given number
"""

import random
import time

print("Choose the number......")
userInput = int(input("Enter any number: "))
time.sleep(3)
takeNumber = int(input("Take the number as same as your original number: "))
print("Number is taken......")
time.sleep(3)

number = random.randint(1, 20)
print("The computer number is: ", number)
time.sleep(3)

sumOfAllNumber = int(input("Add all three number you get: "))
time.sleep(3)

halfOfNumber = float(input("Half the number you get after adding: "))
print("Half of all number....")
time.sleep(3)

subNumber = float(input("Return the number which you take from someone: "))
subNumber = halfOfNumber-takeNumber
print("The remaining number is: ", subNumber)
