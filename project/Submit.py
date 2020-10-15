from tkinter import *
import tkinter.messagebox as tmsg
def mrg():
    mgr = Tk()
    mgr.geometry("700x500")
    mgr.title("Mind Reader Game")

    def final():
        if show_num == cards:
            tmsg.showinfo("Result",f"Your Number is {show_num.get()}")
        else:
            tmsg.showinfo("Result",f"Your Number is {show_num.get()}")
 
    def sub5():
        show_num = [i for i in range(61) if i&32]
        Label(mgr,text=show_num).pack()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        Button(mgr,text="Yes",command=final).pack(side=LEFT)
        Button(mgr,text="No",command=final).pack(side=RIGHT)


    def sub4():
        show_num = [i for i in range(61) if i&16]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr,text="Enter",command=sub5).pack()

    def sub3():
        show_num = [i for i in range(61) if i&8]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr,text="Enter",command=sub4).pack()

    def sub2():
        show_num = [i for i in range(61) if i&4]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr,text="Enter",command=sub3).pack()

    def sub1():
        show_num = [i for i in range(61) if i&2]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr,text="Enter",command=sub2).pack()

    def sub():
        show_num = [i for i in range(61) if i&1]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr, text="Enter",command=sub1).pack()

    def guess():
        global show_num
        num = 0
        valid_entries = ['yes','no']        
        show_num = [i for i in range(61) if i&1]
        Label(mgr,text=show_num).pack()
        yn = StringVar()
        Label(mgr,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.").pack()
        yn_entry = Entry(mgr,textvar=yn)
        yn_entry.pack()
        Button(mgr, text="Enter",command=sub1).pack()

    Label(mgr, text="Weclome to Mind Reader Game",font="Algerian 20 italic").pack()

    my_list = [11,2,8,27,15]
    my_list.reverse()

    def get_binary_function(num):
        return bin(num).replace('0b','')

    cards = [[],[],[],[],[],[]]

    cards = [[[i for i in range(61) if i&2**k][j::5]for j in range(5)] for k in range(6)]

    start = StringVar()
    start = Label(mgr, text="Enter start to continue the game", font="lucida")
    start.pack()
    start_entry = Entry(mgr,textvar=start)
    start_entry.pack()

    Button(mgr,text="Enter",command=guess).pack()

    mgr.mainloop()

mrg()