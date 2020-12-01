import random
import tkinter.messagebox as tmsg
from tkinter import *


def sps():
    sps = Tk()
    sps.geometry("700x500")
    sps.title("Stone Paper Seiccor")
    try:
        
        player_score = 0
        comp_score = 0

        count_rock = count_paper = count_scissors = 0

    # Update Count Function

        def update_count(user_input):
            global count_rock,count_scissors,count_paper
            if user_input == 0:
                count_rock = count_rock+1
            elif user_input == 1:
                count_paper = count_paper+1
            elif user_input == 2:
                count_scissors = count_scissors+1
            else:
                print("Invalid Input!!!!")
        
        # Prediction Function

        def predict():
            if count_rock>count_paper and count_rock>count_scissors:
                pred=0
            elif count_paper>count_rock and count_paper>count_scissors:
                pred=1
            elif count_scissors>count_rock and count_scissors>count_paper:
                pred=2
            else:
                pred = random.randint(0,2)
            return pred
        
        

        # Update Score Function

        def update_score(user_input):
            global player_score
            global comp_score
            pred = predict()
            if user_input==0:
                if pred==0:
                    print("\nYou played ROCK, Computer played ROCK.")
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
                elif pred==1:
                    print("\nYou played ROCK, Computer played PAPER.")
                    comp_score+=1
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
                else:
                    print("\nYou played ROCK, Computer played SCISSOR.")
                    player_score+=1
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
            elif user_input==1:
                if pred==0:
                    print("\nYou played PAPPER, Computer played ROCK.")
                    player_score+=1
                    print("\nComputer Score: ",comp_score, "\nPalyer Score: ",player_score)
                elif pred==1:
                    print("\nYou played PAPER, Computer played PAPER.")
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
                else:
                    print("\nYou played PAPER, Computer played SCISSOR.")
                    comp_score+=1
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
            else:
                if pred==0:
                    print("\nYou played SCISSOR, Computer played ROCK.")
                    comp_score+=1
                    print("\nComputer Score: ",comp_score, "\nPlayer Score: ",player_score)
                elif pred==1:
                    print("\nYou played SCISSOR, Computer played PAPER.")
                    player_score+=1
                    print("\nComputer Score: ",comp_score,"\nPlayer Score: ",player_score)
                else:
                    print("\nYou played SCISSOR, Computer played SCISSOR.")
                    print("\nComputer Score: ",comp_score,"\nPlayer Score: ",player_score)
        
        def sub():
            update_score(user_input)
            update_count(user_input)
            if comp_score==10:
                tmsg.showinfo("Result","Computer Won!!!")
            elif player_score==10:
                tmsg.showinfo("result","You Won!!!")
        
        valid_entries = ['0','1','2']
        pred = predict()
        global user_input
        user_input_var = StringVar()
        user_input = Label(sps,text="Enter 0 for ROCK, 1 for PAPER and 2 for SCISSORS:")
        user_input.pack()
        user_input_entry = Entry(sps,text=user_input_var)
        user_input_entry.pack()
        Button(sps, text="Enter",command=sub).pack()
        
    except Exception as e:
        print(f"Error is {e}")

    sps.mainloop()

if __name__ == "__main__":
    sps()
