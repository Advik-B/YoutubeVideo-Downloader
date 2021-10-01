#NOTE: Only works on windows-10

from win32com.client import Dispatch
from clint.textui import progress
import os
import requests


def download(url:str , output_folder:str , chunk_size:float=1024):
    r = requests.get(url, stream=True)
    path = output_folder.replace('\\' , '/').__add__(f'/{url.split("/")[-1]}')
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=chunk_size), 'progress: ' ,expected_size=(total_length/chunk_size) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

def Create_Shortcut(path:str , start_in:str , name:str) -> None
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop').replace('\\' , '/')
    try:
        f = open(f'{desktop}/desktop.ini' , 'r')
        f.close()
    except FileNotFoundError:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Onedrive\\Desktop').replace('\\' , '/')

    print(desktop) #TODO: Remove later

    Shortcut_path = desktop.__add__(f'/{name}')  # Path to be saved (shortcut)

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(Shortcut_path)
    shortcut.Targetpath = path
    shortcut.WorkingDirectory = start_in
    shortcut.save()