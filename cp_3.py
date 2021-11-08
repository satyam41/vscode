# If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.
# 
# Input
# The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.
# 
# Output
# For each test case, display the sum of first and last digits of N in a new line.
# 
# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 3 
# 1234
# 124894
# 242323
# 
# Output
# 5
# 5
# 5
# 
# def Add(x,y):
#     z = x+y
#     return z
# 
# def FirstAndLast(n):
#     # newn = str(n)
#     newLst = list(n)
#     return Add(newLst[0], newLst[len(newLst)-1])
# 
# 
# num = FirstAndLast(123)
# print(num)

a = 0
while a<=2:
    num = input()
    sums =int(num[0]) + int(num[-1])
    print(sums)
    a+=1
