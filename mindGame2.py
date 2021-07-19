import random
import time

nameOfPlayer = input("Enter your name before play this game: ")
file = open("RecordsOfPlayer.txt", "a")
data = file.write(nameOfPlayer+"\n")
file.close()
print("Your Game will start while.....")
time.sleep(3)

print("Choose the number in your mind between 1-100........")
time.sleep(3)

print("Take the same number from your friend....")
time.sleep(3)

computerNumber = random.randint(1, 10)
print("Take the computer number: ", computerNumber)
time.sleep(3)

print("Add all the number....")
time.sleep(3)

print("Half the number....")
time.sleep(3)

print("Return the number to your friend....")
time.sleep(10)

print("The remaining number is: ", computerNumber/2)
time.sleep(3)
