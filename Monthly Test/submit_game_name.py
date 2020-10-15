from tkinter import *
import tkinter.messagebox as tmsg
import random

root1 = Tk()
root1.geometry("700x500")
root1.title("Stone Paper Seissor")

def update_count(user_input):
    global count_rock, count_paper, count_scissors
    if user_input == 0:
        count_rock = count_rock + 1
    elif user_input == 1:
        count_paper = count_paper + 1
    else:
        count_scissors = count_scissors + 1

        # Create the predict() function.
def predict():
            # Uncomment the lines below.
    if count_rock > count_paper and count_rock > count_scissors:
        pred = 0
    elif count_paper > count_rock and count_paper > count_scissors:
        pred = 1
    elif count_scissors > count_rock and count_scissors > count_paper:
        pred = 2
    else:
        pred = random.randint(0,2)
    return pred

        # Create the player_score and comp_score variables.
player_score = comp_score = 0

def update_scores(user_input):
    global player_score, comp_score
            # Rock wins over scissors, scissors win over paper and paper wins over rock.
    pred = predict()
    if user_input == 0:
        if pred == 0:
            print("\nYou played ROCK, Computer played ROCK.")
            print("\nComputer Score :", comp_score, "\nPlayer Score :", player_score)
        elif pred == 1:
            print("\nYou played ROCK, Computer played PAPER.")
            comp_score += 1
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)
        else:
            print("\nYou played ROCK, Computer Score SCISSOR.")
            player_score += 1
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)
    elif user_input == 1:
        if pred == 0:
            print("\nYou played PAPER, Computer played ROCK.")
            player_score += 1
            print("\nComputer Score :", comp_score, "\nPlayer Score :", player_score)
        elif pred == 1:
            print("\nYou played PAPER, Computer played PAPER.")
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)
        else:# pred == 2:
            print("\nYou played PAPER, Computer Score SCISSOR.")
            comp_score += 1
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)
    else:# user_input == 2:
        if pred == 0:
            print("\nYou played SCISSOR, Computer played ROCK.")
            comp_score += 1
            print("\nComputer Score :", comp_score, "\nPlayer Score :", player_score)
        elif pred == 1:
            print("\nYou played SCISSOR, Computer played PAPER.")
            player_score += 1
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)
        else:# pred == 2:
            print("\nYou played SCISSOR, Computer Score SCISSOR.")
            print("\nComputer Score : ",comp_score," Player Score : ",player_score)

valid_entries = Label(root1, text="['0','1','2']", font="lucida 15 bold")
valid_entries.pack()
valid_entries_var = StringVar()
valid_entries_entry = Entry(root1,text="Enter valid entry", textvar=valid_entries_var)
valid_entries_entry.pack()
Button(root1, text="Enter",command=enter).pack()
# def enter():
while True:
    pred = predict()
    user_input = Label(root1, text="Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ",font="lucida 18 bold")
    user_input.pack()
    user_input_var = StringVar()
    user_input_entry = Entry(root1, text="Enter your choice: ", textvar=user_input_var)
    user_input_entry.pack()
                # user_input = input("Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS : ")
    while user_input not in valid_entries:
        tmsg.showerror("Error", "Invalid Input!!!!!")
        user_input = Label(text="Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS: ",font="lucida 18 bold")
        user_input.pack()
        user_input = int(user_input)
        update_scores(user_input)
        update_count(user_input)
if comp_score == 10:
    tmsg.showinfo("Result","Computer Won!")
    break
elif player_score == 10:
    tmsg.showinfo("Result","You Won!")
    break
    
    root1.mainloop()