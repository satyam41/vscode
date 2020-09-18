from tkinter import *
import tkinter.messagebox as tmsg

def NSPD():
    tmsg.showwarning("Need For Speed Most Wanted","This Game Harm Your Eyes.......")
    nspd = open("Need For Speed", "a")
    nspd.write(f"{namevalue.get()}\n")    
    
def FAUG():
    tmsg.showwarning("FAU-G","This Game Change Your Body Language.......")
    faug = open("FAU-G", "a")
    faug.write(f"{namevalue.get()}\n")
    
def WWE():
    tmsg.showwarning("WWE Raw", "This Game Play Only 15+ Child.......")
    wwe = open("WWE RAW", "a")
    wwe.write(f"{namevalue.get()}\n")
    
def click():
    root_1 = Tk()
    root_1.geometry("700x500")
    root_1.title("List of games")
    
    Label(root_1, text="Need For Speed Most Wanted", font="arialblack 18 bold").pack(ipadx=10, ipady=10)
    Button(root_1, text="Click Here to play", command=NSPD).pack(ipadx=10, ipady=10)     
    
    Label(root_1, text="FAU-G", font="arialblack 18 bold").pack(ipadx=10, ipady=10)
    Button(root_1, text="Click Here to play", command=FAUG).pack(ipadx=10, ipady=10)
    
    Label(root_1, text="WWE RAW", font="arialblack 18 bold").pack(ipadx=10, ipady=10)
    Button(root_1, text="Click Here to play", command=WWE).pack(ipadx=10, ipady=10)
    
    root_1.mainloop()

root = Tk()
root.geometry("500x300")
root.title("Games")

Label(root, text="Want to play games. Click Here", font="algerian 18 bold").pack()

name = Label(root, text="Name : ")
name.pack()

namevalue = StringVar()

name_entry = Entry(root, textvariable=namevalue)
name_entry.pack()

Button(root, text="Click Here", command=click).pack(ipadx=15, ipady=15,padx=10, pady=10)

root.mainloop()