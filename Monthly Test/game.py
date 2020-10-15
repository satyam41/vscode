from tkinter import *
from submit import *
from click_here import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("700x500")
root.title("Games")

def player_name():
    palyer = open("Name of Player.txt",'a')
    data = f"{namevar.get()}\n"
    palyer.write(data)
    palyer.close()

Label(text="Welcome to the Game of World", font="algerian 20 bold").pack(ipadx=10,pady=10)

name = Label(text="Enter your name: ", font="lucida 15 bold")
name.pack()

namevar = StringVar()

name_entry = Entry(text="Enter your name: ", textvariable=namevar)
name_entry.pack()

Button(text="Submit",command=player_name).pack(ipadx=10,padx=5,pady=5)

Label(text="Want to See list of Games", font="Harrington 18 bold").pack()

Label(text="OR", font="Harrington 18 bold").pack()

Label(text="List of Games. Choose your choice you want to play....", font="Harrington 18 bold").pack()

Button(text="Click Here to see list of Games", command=click).pack(ipadx=10,padx=5,pady=5)

root.mainloop()