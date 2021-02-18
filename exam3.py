def reverse(x):
    x.reverse()
    double = []
    for i in x:
        double.append(i*2)
    return double

lst = [1,2,3,4,5]
print(reverse(lst))