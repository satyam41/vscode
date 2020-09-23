"""if, elif and else statement.

age = int(input("Enter your age : "))
age = 15
if age >= 10 and age < 18:
    print("You drive a cycle.")
elif age < 10:
    print("You can not drive any thing.")
else:
    print("You can drive cycle as well as bike, car etc.")

a = b = c = 0
for i in range(2):
    a = 10
    b = 5
    if b == 0:
        print("Division by zero error! Aborting!")
        break
    else:
        c = a/b
        print("Quotient =", c)
print("Program Over!!!")


Question of the day: Print the table."""