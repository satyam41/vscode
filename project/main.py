from tkinter import *
import Sps
import Mrg
import Hat

main = Tk()
main.geometry("300x200")
main.title("")

def submit():
    root = Tk()
    root.geometry("700x500")
    root.title("")

    with open("username.txt",'a') as f1:
        f1.write(f"{name_entry.get()}\n")

    Label(root, text="WelCome to World of Games",font="Algerian 20 italic").pack(ipadx=10,padx=10,pady=5,ipady=5)

    Label(root, text="Stone Paper Seiccor",font="lucida 15 bold").pack(ipadx=10,padx=10,pady=5,ipady=5)
    Button(root, text="Play Game",cursor="dotbox",command=Sps.sps).pack(ipadx=10,padx=10,pady=5,ipady=5)

    Label(root, text="Mind Reader Game",font="lucida 15 bold").pack(ipadx=10,padx=10,pady=5,ipady=5)
    Button(root, text="Play Game",cursor="dotbox",command=Mrg.mrg).pack(ipadx=10,padx=10,pady=5,ipady=5)

    Label(root, text="Head And Tail",font="lucida 15 bold").pack(ipadx=10,padx=10,pady=5,ipady=5)
    Button(root, text="Play Game",cursor="dotbox",command=Hat.hat).pack(ipadx=10,padx=10,pady=5,ipady=5)

    Button(root, text="Exit",command=quit).pack(ipadx=10,padx=10,pady=5,ipady=5)


    root.mainloop()

name = StringVar()
Label(main,text="Enter Your Name: ",font="Algerian 20 roman").pack(ipadx=10,padx=10,pady=5,ipady=5)
name_entry = Entry(main, textvar=name,font="Harrington 15 bold")
name_entry.pack()

Button(main, text="Submit",cursor="dotbox",command=submit).pack(ipadx=10,padx=10,pady=5,ipady=5)
Button(main, text="Exit",command=quit).pack(ipadx=10,padx=10,pady=5,ipady=5)

main.mainloop()