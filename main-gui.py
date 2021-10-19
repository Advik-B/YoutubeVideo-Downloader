import os
from threading import Thread
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from ttkthemes import themed_tk as tk

from PIL import Image

from functions import *
from search import *
# from sounds import *

def cls():

    """Will clear the screen
    """

    os.system('cls')

def clear():

    """Will clear the screen
    """

    os.system('cls')
    

app = tk.ThemedTk()
screen_width = int(app.winfo_screenwidth())
screen_height = int(app.winfo_screenheight())

app_height = int(screen_height * .6)
app_width = int(screen_width * .5)

app_gm_1 = int(screen_width * .25)
app_gm_2 = int(screen_height * .1)
del screen_width
del screen_height

app.geometry(f'{app_width}x{app_height}+{app_gm_1}+{app_gm_2}') # You can adjust it later


if __name__ == '__main__':
    # Mainloop
    app.mainloop()


#NOTE: Work in progress 😅
