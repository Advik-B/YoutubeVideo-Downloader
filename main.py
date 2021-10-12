import os

from threading import Thread

from tkinter import *

from tkinter import filedialog, messagebox, ttk


from PIL import Image


from functions import *

from search import *

from sounds import *



def cls():

    """Will clear the screen
    """

    os.system('cls')


def clear():

    """Will clear the screen
    """

    os.system('cls')
    

app = Tk()

app.geometry('800x600+600+200')


# Screen-1
scr1 = ttk.Notebook()
# Mainloop
app.mainloop()


#NOTE: Work in progress 😅