# Define a function to print the list to interchange the first element with last element.

def swapList(newList):
    size = len(newList)

    lst = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = lst

    return newList

lst = [1,2,3,4,5]
print(swapList(lst))