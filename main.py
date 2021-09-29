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
    print(system())
    os.system('cls')

def clear():
    cls()

#NOTE: Work in progress 😅