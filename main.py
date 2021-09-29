from threading import Thread
from platform import system
from subprocess import call
from time import sleep
try:
    from functions import *
    from search import *
    from sounds import *
except ModuleNotFoundError:
    from platform import system
    from subprocess import run
    call('python -m pip install -r requirements.txt' , shell=True)
    sleep(10)
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