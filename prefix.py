# Write a program that prompt the user for two strings and checks if the strings is a prefix of the other. Print an appropriate message to inform the user which is the prefix of which or that neither is a prefix. For example, if the user input "evergreen" and "ever", the program would respond: "ever" is a prefix of "evergreen". But if the input was "evergreen" and "green", the program would respond that neither is a prefix of the other.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if string1.startswith(string2):
    print(f"{string2} is a prefix of {string1}")
else:
    print("Neither is a prefix of the other.")
