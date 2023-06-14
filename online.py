a = input("Enter the price of A.C.: ")
b = input("Enter the price of A.C.: ")
c = input("Enter the price of A.C.: ")
d = input("Enter the price of A.C.: ")

#price = 1<= (a,b,c,d) <= 10**6

less_a = b,c,d
less_b = a,c,d
less_c = a,c,d
less_d = a,b,c

if a < less_a:
    print(a)
elif b < less_b:
    print(b)
elif c < less_c:
    print(c)
elif d < less_d:
    print(d)
