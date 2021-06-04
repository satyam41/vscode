# Write a program to input marks in 3 subjects; compute average and then calculate grade as per following guidelines:

"""
Grade           Marks
 A           80% and above
 B           70-79%
 C           60-69%
 D           50-59%
 E           40-49%
 R           39% and below
"""


def Percentage(val1, val2, val3):
    avg = val1 + val2 + val3
    percent = (avg / 300)*100
    return percent


sub1 = int(input("Enter the number of subject 1: "))
sub2 = int(input("Enter the number of subject 2: "))
sub3 = int(input("Enter the number of subject 3: "))
average = Percentage(sub1, sub2, sub3)
print(average, "%")

if average >= 80:
    print("You have assigned Grade A.")
elif 70 <= average < 80:
    print("You have assigned Grade B")
elif 60 <= average < 70:
    print("You have assigned Grade C")
elif 50 <= average < 60:
    print("You have assigned Grade D")
elif 40 <= average < 50:
    print("You have assigned Grade E")
elif average < 40:
    print("You have assigned Grade R\nYou are fail....")

