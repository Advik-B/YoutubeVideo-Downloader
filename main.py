from threading import Thread
from platform import system
from subprocess import run
from time import sleep
import os
try:
    from functions import *
    from search import *
    from sounds import *
    from PIL import Image
except ModuleNotFoundError:
    run('python -m pip install -r requirements.txt' , shell=True)
    from functions import *
    from search import *
    from sounds import *
    from PIL import Image
#TODO: add support to use optprase module

# -Functions-
def cls():
    platform = system().casefold()

    if platform == 'windows':
        run('cls' , shell=True)
    elif platform == 'linux' or platform == 'darwin' or platform == 'mac':
        run('clear' , shell=True)
    else:
        run('clear' ,shell=True)

def clear():
    cls()

cls()

menu_dict = {

    1:'search',
    2:'link',

}

menu_dict2 = {}

for key , val in menu_dict.items():
    menu_dict2.update({val:key})

print(menu_dict2)

menu = f"""\n

--------------
| 1 | {menu_dict[1]} |
| 2 | {menu_dict[2]}   |
--------------
"""


while True:
    print('How do you want download your video?')
    print(menu)

#NOTE: Work in progress 😅