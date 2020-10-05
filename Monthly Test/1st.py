import math, numpy as np, random, string, first_letter
# print(math.pi)

a = np.divmod(12,6)
# print(a)

# print(max([100,5,9,10,77,4],[6]))

# print(oct(15))
# print(hex(15))

# print(round(3.2,6))

a = "I Love My India".split()
# print(type(a))
a = "I Love My India".split(" ")
# print(len(a))

a = "I LOVE MY INDIA".replace("INDIA", "BHARAT")
# print(a)

a = '///'.join("Hi Satyam")
# print(a)


a = random.uniform(2.5,65.7)
# print(a)

a = random.randrange(start=2, stop=5)
# print(a)

a = random.random()
# print(a)

# print(string.ascii_letters)


name = "Jayant"
surname = "Hari"
print(f"Your first name and last name of the first letter is {first_letter.name_of_first_letter(name,surname)} and your name is {name} {surname}")