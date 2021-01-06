lst = [2,5,4,7,6]
lst.sort()
min = 1
for i in range(1,len(lst)):
    min = min*lst[i]
print("Maxmimum", min)
lst.sort(reverse=True)
max = 1
for j in range(1,len(lst)):
    max = max*lst[j]
print("Minimum", max)


lst1 = []
num = int(input("Enter any number : "))
for i in range(1,num):
    if num%i == 0:
        lst1.append(i)
print(lst1)
