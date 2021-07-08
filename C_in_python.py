# Write a program to find out whether a student is pass or fail; if it requires total 40% and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from user.

chm = eval(input("Enter the marks of the Chemistry pre-board exam out of 70: "))
eng = eval(input("Enter the marks of the English pre-board exam out of 80: "))
cs = eval(input("Enter the marks of the CS pre-board exam out of 70: "))

chm_per = chm / 70 * 100
eng_per = eng / 80 * 100
cs_per = cs / 70 * 100

sum_of_marks = chm + eng + cs
percent = sum_of_marks / 220 * 100

if percent >= 40 and chm_per >= 33 and eng_per >= 33 and cs_per >= 33:
    print(percent)
    print("You are pass!!!")
else:
    print("You are fail.")
