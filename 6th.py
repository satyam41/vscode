"""list is a type of data storage.
It is use to store data which we want to change any time without any error.

empty_list = []
non_empty_list = [1,2,3,4,5]

functions of the list:
    1. list.append(element) - it add items in the end of the list.
    2. list.clear() - it clear the whole list.
    3. list.copy() - it copy the whole list.
    4. list.count(element) - it count the duplicate element present in the list.
    5. list.extend(list) - it add two list in one list.
    6. list.index(n) - it show the index of the element.
    7. list.insert(index, element) - it insert element into the list.
    8. list.remove(element) - it removes the element to the list.
    9. list.reverse() - it reverse the list.
    10. list.sort() - it sort the list in assending order.
    11. list.pop([index number]) - it remove the element to the list from end.

lst = [1,2,3,4,5]
# print(lst)
# using of functions of list.
# 1. list.append()
lst.append(6)
# print(lst)
Output: [1,2,3,4,5,6]

# 2.list.extend()
lst2 = ['a','b','c']
lst.extend(lst2)
# print(lst)
Output: [1,2,3,4,5,6,'a','b','c']

# 3.list.index()
index = lst.index('a')
# print(index)
Output: 6

# 4. list.insert()
lst.insert(6,7)
# print(lst)
Output: [1,2,3,4,5,6,7,'a','b','c']

# 5. list.pop(index)
lst.pop(6)
# print(lst)
Output: [1,2,3,4,5,6,'a','b','c']

# 6. list.remove()
lst.remove(3)
# print("After copy the list", lst)
Output: [1,2,4,5,6,'a','b','c']

# 7. list.copy()
copy = lst.copy()
# print("Before Copy the list", copy)
Output: it print same list.

# 8.list.clear()
# print("List after clear", lst)
clear = lst.clear()
# print("List before clear", lst)
Output: [] # it return empty list.

# 9. list.count()
l = [2,4,4,5,2,4,2,6,6,8,7,8,7,8]
count = l.count(2)
# print("Count function is work like this", count)
Output: 3

# 10.list.sort()
l2 = [2,4,3,1,5]
# print("List after reverse sorting", l2)
l2.sort()
# print("List before sorting", l2)
Output: [1,2,3,4,5]

# 11. list.reverse()
l2.sort(reverse=True)
# print("List before reverse sorting", l2)
Output: [5,4,3,2,1]
"""
