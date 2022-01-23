"""A list within another list is called a nested list.

lst1 = [29, 12]
lst2 = [40, 23, 21, lst1]
print(lst2)
# print(lst2[3][0])
for i in lst2[3]:
    print(i)

# A Python program tp create a nested list and display elements.
lst = [1,2,3,4,5,[10, 20]]
print("Total list = ",lst)
print("Display first element of the list = ",lst[0])
print("Nested list = ",lst[5])
for i in lst[5]:
    print(i)"""

# Nested List as Matrices

"""mat = [[1,2,3],[4,5,6],[7,8,9]]
# print(mat)

# if we use a foor loop to retrieve the elements from 'mat', it will retrieve row by row, as:
for r in  mat:
    print(r)

# but we want to retrieve columns (or elements) in each row; hence we need another for loop inside the previous loop, as:
for r in mat:
    for c in r: # display coloumns in each row.
        print(c, end=' ')
    print()"""

# II Method

mat = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(mat)): # i values change from 0 to m-1
    for j in range(len(mat[i])): # j values changes from 0 to n-1.
        print("%d" %mat[i][j], end=' ')
    print()