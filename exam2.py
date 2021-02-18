def push(arr):
    newArr = []
    for num in arr:
        if num%2==0:
            pass
        else:
            newArr.append(num)
    return newArr

lst = [1,2,3,4,5,7,9]
print(push(lst))