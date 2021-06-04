# Write a function that takes a character (i.e., a string of length 1) and return True if it is a vowel, False otherwise.

def Vowel(userInput):
    if userInput == 'a' or userInput == 'e' or userInput == 'i' or userInput == 'o' or userInput == 'u':
        return True
    else:
        return False


print(Vowel('u'))
