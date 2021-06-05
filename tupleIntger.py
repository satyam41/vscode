# Write a program that inputs a number n(integer) and creates a tuple containing n, 2n, 3n, and 4n.

lst = []
n = int(input("Enter any number: "))
for i in range(4):
    lst.append((i + 1) * n)  # 1*5, 2*5, 3*5, 4*5
tup = tuple(lst)
print(tup)
