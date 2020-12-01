from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("700x550")
root.title("")

def get_binary_digits(dividend):
  binary_digits = []
  while dividend != 0:
    quot = dividend // 2
    remainder = dividend % 2
    binary_digits.append(remainder)
    dividend = quot # The quotient becomes the new dividend. 
  binary_digits.reverse()
  return binary_digits



cards = [[] for i in range(6)]
#cards


first_six_powers_of_two = [2 ** i for i in range(6)]

for num in range(1, 64):
  bin_digs = get_binary_digits(num)
  for i in range(len(bin_digs)):
    power_of_two = 2 ** ((len(bin_digs) - 1) - i)
    if bin_digs[i] * power_of_two in first_six_powers_of_two:
      cards[(len(bin_digs) - 1) - i].append(num)



def next():
    num = 0
    if quest == 'yes':
        num = num + cards[i][0]
      
# Print the value of the 'num' variable.
    tmsg.showinfo("Result",f"\nYou thought of the number {num}")



def start():
    global quest
    for i in range(len(cards)):
        Label(root,text=f"Does your number exist on Card {i + 1},{?Card}, {i + 1}, {==>}, cards[i]")
        quest = StringVar()
        quest = Label(root,text="Enter either yes or no:\n")
        quest.pack()
        quest_entry = Entry(root, text=quest)
        quest_entry.pack()
        Button(root,text="Next",command=next).pack()

player_input = StringVar()
player_input = Label(root,text="Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.\n")
player_input.pack()
player_input_entry = Entry(root,text=player_input)
player_input_entry.pack()
Button(root,text="Start",command=start).pack()
# Keep printing the message until the player enters only 'start'.
#while player_input != 'start':
 #   player_input = StringVar()
  #  player_input = Label(root, text="Think of a number between 1 and 63. Type 'start' when you are ready and hit the 'Enter' key.\n")
   # player_input.pack()
    #player_input__entry = Entry(root, text=start)
    #player_input_entry.pack()
# Create the 'num' variable and set its initial value equal to 0.
num = 0

# Create a list named valid_entries.
valid_entries = ['yes', 'no']

# Create a loop to display the numbers of each card and to take the input whether the number exists in the card displayed. 

#while quest_entry not in valid_entries:
 #   print("Does your number exist on Card", i + 1,"?\nCard", i + 1, "==>", cards[i])
  #  quest = StringVar()
   # quest = input("Enter either yes or no:\n")
    #quest.pack()
    #quest_entry = Entry(root, text=quest)
    #quest_entry.pack()
  
  # If the number exists in the card displayed, then add the first number to the 'num' variable. Use list indexing, to get the first number.


root.mainloop()
