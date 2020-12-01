from tkinter import *
import tkinter.messagebox as tmsg

mind = Tk()
mind.geometry("1000x900")
try:
    def enter():
        pass


    def start():
        valid_entries = ['Yes','No']
        show_num = [i for i in range(61) if i&1]
        Label(mind,text=show_num).pack()
        yn = StringVar()
        yn = Label(mind,text="Enter your number is exist in the first card. If yes write 'YES' or no write 'NO'.")
        yn.pack()
        yn_entry = Entry(mind, text=yn)
        yn_entry.pack() 
        Button(mind, text="Enter1",command=enter).pack()


    cards = [[],[],[],[],[],[]]
    
    def get_binary_function(num):
        return bin(num).replace('0b','')
    
    cards = [[[i for i in range(61) if i&2**k][j::5]for j in range(5)] for k in range(6)]


    Label(mind, text="Think of a number between 1 to 63").pack()
    start = StringVar()
    start = Label(mind, text="Enter 'START' to proceed the game")
    start.pack()
    start_entry = Entry(mind,text=start)
    start_entry.pack()
    Button(mind,text="START",command=start).pack()

except Exception as e:
    print(f"Error Raised is {e}")


mind.mainloop()