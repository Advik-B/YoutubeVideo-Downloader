import os
import shutil
from threading import Thread
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk
from ttkthemes import themed_tk as tk

from functions import *
from search import *

global STATE
STATE = False
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


app.geometry(f'{app_width}x{app_height}+{app_gm_1}+{app_gm_2}') # You can adjust it later

# Prepping the screen
screen = ttk.Notebook(app, padding=3)
screen.pack(fill=BOTH, expand=True)
# Screen-1: download with link
with_link = Frame(screen, bg='#2b2d37',)
help_wl =ttk.Label(with_link, text='Paste the link below:' , foreground='white', background='#2b2d37' ,font='Vendara 18')
link_var_wl = StringVar()
link_wl = ttk.Entry(with_link ,background='#2b2d37', textvariable=link_var_wl, width=44, font=['Ubuntu Mono', 14], foreground='#2b2d37', takefocus=True)

help_btn_wl = Button(with_link, activebackground='#2b2d37', text='help', borderwidth=0, border=0 ,activeforeground='#2b2d37', background='#2b2d37',fg='#2b2d37')

class temp():
    def __init__(self) -> None:
        self.STATE = STATE
    
    def _validate_link(self):
        try:
            valid_img = ImageTk.PhotoImage(image=Image.open('assets/icons/valid.png'))
            invalid_img = ImageTk.PhotoImage(image=Image.open('assets/icons/invalid.png'))
            checkin_img = ImageTk.PhotoImage(image=Image.open('assets/icons/~.png'))
            
            def leave(page):
                os.system(f'taskkill /f /im ytdl.exe')
                global running
                running = False
                print(page)
                app.destroy()
                app.quit()
                exit(0)
            running = True         
            
            app.bind('<Escape>', leave)
            def invalid():
                messagebox.showerror('Error' , 'Invalid YouTube link')
            def checkin():
                messagebox.showinfo('Info', 'No link is provided')
            def valid(LINK:str):
                messagebox.showinfo('Info', "The link: '%s' is a valid video link!" % LINK)

            while running:
                if running:
                    try:
                        LINK = link_var_wl.get()
                        if LINK:
                            if 'youtube.com' in LINK and len(LINK) >= 42 and len(LINK) <= 43:
                                try:
                                    ś = vid_exists(LINK)
                                    if ś == True:
                                        help_btn_wl.config(image=valid_img, command=lambda:valid(LINK))
                                        self.STATE = True
                                        
                                    elif ś == False:
                                        help_btn_wl.config(image=invalid_img, command=invalid)
                                        self.STATE = False
                                        continue
                            
                                except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL):
                                    help_btn_wl.config(image=invalid_img, command=invalid)
                                    self.STATE = False
                                    continue
                            else:
                                help_btn_wl.config(image=invalid_img, command=invalid)
                                self.STATE = False
                                continue

                        else:
                            help_btn_wl.config(image=checkin_img, command=checkin)
                            self.STATE = False
                    except RuntimeError:
                        exit(0)
                elif running == False: exit(0)
        except RuntimeError: exit(0)
def download_av():
    global æ_


    link = link_var_wl.get()
    messagebox.showinfo('Info', 'Downloading video:\n the video will open when it is completed')
    ṣ = lambda: download_AV(link)
    ṣ_ = Thread(target=ṣ)
    ṣ_.start()
    def ñ():
        while True:
            v1 = os.listdir(os.getcwd())
            for f in v1:
                if f.endswith('.mp4'):
                    vid_fol = os.path.join(os.path.join(os.path.expanduser('~')), 'Videos')
                    a = shutil.move(os.path.join(os.getcwd(), f), vid_fol)                           
                    if messagebox.askyesno('Sucess', 'The video has been downloaded. Do you want to view it?') == True:
                        os.system('explorer.exe "%s"' % a)
                        exit(0)
    Q = Thread(target=ñ)
    Q.start()

  
download_btn = ttk.Button(with_link, text='Download', command=download_av)

help_wl.grid(row=0, ipady=30, columnspan=100, column=0)
link_wl.grid(row=1, padx=80, column=0)
help_btn_wl.grid(row=1, column=0, sticky=E,)
download_btn.grid(row=2, column=0, columnspan=100)

if __name__ == '__main__':
    # Mainloop
    screen.add(with_link, text='Download with link')
    app.config(bg='#2b2d37')
    app.set_theme('plastik')
    app.resizable(False, False)
    
    WX = temp()
    æ_ = Thread(target=WX._validate_link)
    æ_.start()
    app.mainloop()
    os.system('taskkill /f /im ytdl.exe')


#NOTE: Work in progress 😅
