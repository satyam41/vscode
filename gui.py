from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("700x300")
root.title("Games")

def lol():
    msg.showwarning("NSPD", "Games is harm your eyes.......")

def click():
    root1 = Tk()
    root1.geometry("700x300")
    root1.title("Need For Speed Most Wanted")
    
    Label(root1, text="Welcome to NEED FOR SPEED MOST WANTED", font="algerian 20 bold").pack()
    Button(root1, text="Click here to entered in the game.", command=lol).pack()

    root1.mainloop()

Label(root, text="Want to Play Games. Click the button.", font="comicsansms 20 bold").pack(padx=5,pady=5)
Button(root, text="Click Here", command=click).pack(ipadx=10, ipady=10)

root.mainloop()