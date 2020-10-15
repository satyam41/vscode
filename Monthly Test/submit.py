from tkinter import *
import tkinter.messagebox as tsmg
from click_here import click

def Submit():   

    Label(text="Want to play games to click here", font="Harrington 20 bold").pack()

    Button(text="CLICK HERE",command=click).pack()