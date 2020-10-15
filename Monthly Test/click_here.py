from tkinter import *
import tkinter.messagebox as tmsg

def click():
    def sub():
        with open("Name of Game.txt",'a') as f1:
            data_entry = f"{check1.get()}\n"
            f1.write(data_entry)
        tmsg.showwarning("Result", "Its Harms your Eyes...")
    
    Label(text="1.Stone Paper Seissor",font="lucida 11 bold").pack()
    Label(text="2.Need for Speed",font="lucida 11 bold").pack()
    Label(text="3.Just Cause",font="lucida 11 bold").pack()
    Label(text="4.Fifa 2020",font="lucida 11 bold").pack()

    check1 = StringVar()
    check1_entry = Entry(text="Entre Your Choice: ",textvar=check1)
    check1_entry.pack()

    Button(text="Submit",command=sub).pack()