L = [1,2,3,4,6,7,8]
item = eval(input("pl enter any number: "))
LB = 0
UB = len(L)-1
while LB<UB:
    if L[LB]<=item and item<=L[LB+1]:
        pos = LB+1
        break
    else:
        LB = LB+1
        continue
if LB==UB:
    pos = UB +1
while UB>=pos:
    temp = L[pos]
    UB=UB-1
L.insert(L[pos-1],item)
print(L)
