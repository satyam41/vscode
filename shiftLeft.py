# Write a function LShift(Arr,n) in Python, which accepts a list Arr of numbers and n is a numeric value by which all elements of the list are shifted to left. Sample Input Data of the list:
# Arr= [ 10,20,30,40,12,11], n=2
# Output
# Arr = [30,40,12,11,10,20]

def LShift(arr, n):
    lst = []
    n -= 1
    while n >= 0:
        a = arr[n]
        lst.append(a)
        arr.pop(n)
        n -= 1
    l = len(lst)
    for i in range(-1, -l - 1, -1):
        arr.append(lst[i])
    print(arr)


Arr = [10, 20, 30, 40, 12, 11]
LShift(Arr, 2)
