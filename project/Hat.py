from tkinter import *
import random
import tkinter.messagebox as tmsg

def hat():
    global ctr
    game_3 = Tk()
    game_3.geometry("700x800")
    game_3.title("")

    def continue_game():
        if guess_entry == number:
            tmsg.showinfo("Result","You Win!!!")
            # break
        else:
                ctr += 1
        if not ctr<5:
            tmsg.showinfo("Result", f"You lose : (\n The number was {number}")

    global ctr, guess_entry, number
    number = random.randint(10,50)
    ctr = 0
    for i in range(ctr < 5):
        guess = StringVar()
        guess = Label(game_3, text="Guess a number in range of 10..50: ")
        guess.pack()
        guess_entry = Entry(game_3,text=guess)
        guess_entry.pack()
        Button(game_3,text="Enter",command=continue_game).pack()
        
    game_3.mainloop()

if __name__ == "__main__":
    hat()
