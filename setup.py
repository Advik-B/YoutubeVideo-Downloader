#NOTE: Only works on windows-10

from win32com.client import Dispatch
from clint.textui import progress
from sys import stdout
from subprocess import run
from time import sleep
from itertools import cycle
from threading import Thread
import os
import requests
import tempfile
import shutil

loading_chars = cycle('/-\|')


def download(url:str , output_folder:str , chunk_size:float=1024):
    r = requests.get(url, stream=True)
    path = output_folder.replace('\\' , '/').__add__(f'/{url.split("/")[-1]}')
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=chunk_size), 'progress: ' ,expected_size=(total_length/chunk_size) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

def Create_Shortcut(path:str , start_in:str , name:str) -> None:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop').replace('\\' , '/')
    try:
        f = open(f'{desktop}/desktop.ini' , 'r')
        f.close()
    except FileNotFoundError:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Onedrive\\Desktop').replace('\\' , '/')

    print('Creating Shortcut here:',desktop) #TODO: Remove later

    Shortcut_path = desktop.__add__(f'/{name}')  # Path to be saved (shortcut)

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(Shortcut_path)
    shortcut.Targetpath = path
    shortcut.WorkingDirectory = start_in
    shortcut.save()

def cls():
    run('cls' , shell=True)

def __setup():
    print('\n\rDownloading app files...')
    tempdirpath = tempfile.mkdtemp()
    download('https://github.com/Advik-B/YoutubeVideo-Downloader/raw/virtualenv/YoutubeVideo-Downloader.zip' , tempdirpath)
    print('\n\nDone!')
    sleep(4.5)
    cls()

    local_appdata = os.path.expandvars(r'%LOCALAPPDATA%')



    download('https://github.com/Advik-B/YoutubeVideo-Downloader/raw/virtualenv/YTDL.zip')


    
    shutil.rmtree(tempdirpath , ignore_errors=True)

T = Thread(target=__setup)
def setup():
    T.start()

setup()
# def scrwrite():
#     while True:

#         stdout.write(f'\rSetup is running {next(loading_chars)}')
#         sleep(.7)

# S = Thread(target=scrwrite)
# S.start()