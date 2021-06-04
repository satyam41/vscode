# Twisted pig latin. Prompt the user to enter a single word. Then form a new word by taking the first letter of the original word, moving it to the end, and adding "ay". Thus "school" becomes "choolsay".

userWord = input("Enter you word: ")
newWord = userWord.replace(userWord[0], userWord[len(userWord)-1])
newWord = newWord.removeprefix(newWord[0])
newWord = newWord + userWord[0] + "ay"
print(newWord)
