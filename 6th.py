"""list is a type of data storage.
It is use to store data which we want to change any time without any error.

empty_list = []
non_empty_list = [1,2,3,4,5]

functions of the list:
    1. list.append()
    2. list.clear()
    3. list.copy()
    4. list.count()
    5. list.extend()
    6. list.index()
    7. list.insert()
    8. list.remove()
    9. list.reverse()
    10. list.sort()
    11. list.pop()

lst = [1,2,3,4,5]
# print(lst)
# using of functions of list.
# 1. list.append()
lst.append(6)
# print(lst)

# 2.list.extend()
lst2 = ['a','b','c']
lst.extend(lst2)
# print(lst)

# 3.list.index()
index = lst.index('a')
# print(index)

# 4. list.insert()
lst.insert(6,7)
# print(lst)

# 5. list.pop(index)
lst.pop(6)
# print(lst)

# 6. list.remove()
lst.remove(3)
# print("After copy the list", lst)

# 7. list.copy()
copy = lst.copy()
# print("Before Copy the list", copy)

# 8.list.clear()
# print("List after clear", lst)
clear = lst.clear()
# print("List before clear", lst)

# 9. list.count()
l = [2,4,4,5,2,4,2,6,6,8,7,8,7,8]
count = l.count(2)
# print("Count function is work like this", count)

# 10.list.sort()
l2 = [4,6,2,1,9,0,6,3]
# print("List after reverse sorting", l2)
l2.sort()
# print("List before sorting", l2)

# 11. list.reverse()
l2.sort(reverse=True)
# print("List before reverse sorting", l2)"""