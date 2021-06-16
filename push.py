def push(lst, n):
    lst.append(n)
    print("Item is added into the list.")

def Pop(lst):
    lst.pop()
    print("Item is remove successfully.")

l = []
push(l, 4)
print(l)
Pop(l)
print(l)
