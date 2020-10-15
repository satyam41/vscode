# import math, numpy as np, random, string, first_letter
# # print(math.pi)

# a = np.divmod(12,6)
# # print(a)

# # print(max([100,5,9,10,77,4],[6]))

# # print(oct(15))
# # print(hex(15))

# # print(round(3.2,6))

# a = "I Love My India".split()
# # print(type(a))
# a = "I Love My India".split(" ")
# # print(len(a))

# a = "I LOVE MY INDIA".replace("INDIA", "BHARAT")
# # print(a)

# a = '///'.join("Hi Satyam")
# # print(a)


# a = random.uniform(2.5,65.7)
# # print(a)

# a = random.randrange(start=2, stop=5)
# # print(a)

# a = random.random()
# # print(a)

# # print(string.ascii_letters)


# name = "Jayanti"
# surname = "Hari"
# print(f"Your first name and last name of the first letter is {first_letter.name_of_first_letter(name,surname)} and your name is {name} {surname}")

# Write your code here.
num = int(input("Enter number: "))
temp = num
new_num = 0
while num>=1:
    revnum = num%10
    new_num = (new_num*10)+revnum
    new_num = new_num // 10
if new_num == temp:
    print(f"{new_num} is a palidrome.")
else:
    print(f"{new_num} is not a palidrome.")
