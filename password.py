# Write a program that prompt a user for their "password" and then determines if the password is valid or not. A password is said to be valid if it starts with a digit and it has length 6 or more. If your program determines that the user-entered password is not valid, it should print a message saying so. Otherwise, it should print a message saying that it has accepted the user-entered password.

def CheckPassword(password):
    """
    :param password: length of password is 6 or more and valid password is starting with digit
    :return: is password is valid or not valid
    """
    if password.isdigit() and len(password) >= 6:
        return "User-entered password is valid"
    else:
        return "User-entered password is not valid.....\nPassword:length 6 or more, start with any digit."


userInput = input("Enter your password: ")
userInput = CheckPassword(userInput)
print(userInput)


