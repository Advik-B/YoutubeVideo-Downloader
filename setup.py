#NOTE: Only works on windows-10

from win32com.client import Dispatch
from clint.textui import progress
from sys import stdout
from subprocess import run
from time import sleep
from threading import Thread
from zipfile import ZipFile
import os
import requests
import tempfile
import shutil


def download(url:str , output_folder:str , chunk_size:float=1024):
    r = requests.get(url, stream=True)
    path = output_folder.replace('\\' , '/').__add__(f'/{url.split("/")[-1]}')
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=chunk_size), 'progress: ' ,expected_size=(total_length/chunk_size) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

def Create_Shortcut(path:str , start_in:str , name:str , args:str, icon:str) -> None:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop').replace('\\' , '/')
    try:
        f = open(f'{desktop}/desktop.ini' , 'r')
        f.close()
    except FileNotFoundError:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Onedrive\\Desktop').replace('\\' , '/')

    Shortcut_path = desktop.__add__(f'/{name}')  # Path to be saved (shortcut)

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(Shortcut_path)
    shortcut.Targetpath = path
    shortcut.WorkingDirectory = start_in
    shortcut.Arguments = args
    shortcut.IconLocation = icon
    shortcut.save()

def cls():
    run('cls' , shell=True)

def __setup():
    print('\n\rDownloading app files ...')
    tempdirpath = tempfile.mkdtemp()
    download('https://github.com/Advik-B/YoutubeVideo-Downloader/raw/virtualenv/YoutubeVideo-Downloader.zip' , tempdirpath)
    print('\n\nDone!')
    sleep(2.5)
    cls()

    local_appdata = os.path.expandvars(r'%LOCALAPPDATA%')

    AppFolder = os.path.join(local_appdata , 'YouTube-VID Downloader')

    AppRuntimeFolder = os.path.join(AppFolder , 'runtime')
    
    os.mkdir(AppFolder)
    os.mkdir(AppRuntimeFolder)

    for files in os.walk(tempdirpath):
        file = os.path.join(files[0] , files[2][0])
        shutil.move(file , AppFolder)


    sleep(2.5)
    cls()

    print('Extracting app files ...')

    for file in os.walk(AppFolder):
        file = os.path.join(file[0] , *file[2])

        if str(file).endswith('.zip'):
            with ZipFile(file , 'r') as zip:
                zip.extractall(AppFolder)
            os.remove(file)
        
    print('Done!')
    sleep(2.5)
    cls()
    print('Downloading runtime ...')

    download('https://github.com/Advik-B/YoutubeVideo-Downloader/raw/virtualenv/app-runtime.zip' , tempdirpath)

    print('Done!')
    sleep(2.5)
    cls()

    print('Extracting runtime ...')
    for files in os.walk(tempdirpath):
        file = os.path.join(files[0] , *files[2])

        shutil.move(file , AppRuntimeFolder)
    
    for file in os.walk(AppRuntimeFolder):
        file = os.path.join(file[0] , *file[2])

        if file.endswith('.zip'):
            with ZipFile(file , 'r') as zip:
                zip.extractall(AppRuntimeFolder)
            os.remove(file)
        
    print('Done!')
    sleep(2.5)
    cls()
    AppIconFolder = os.path.join(AppFolder , 'icons')
    os.mkdir(AppIconFolder)

    print('Downloading icon ...')
    download('https://github.com/Advik-B/YoutubeVideo-Downloader/raw/virtualenv/icon.ico' , AppIconFolder)

    print('Done!')
    sleep(2.5)
    cls()

    print('Creating Shortcut ...')
    

    
    ico_path = os.path.join(AppIconFolder , 'icon.ico')
    
    mainapp = os.path.join(AppFolder, 'main.py')
    runtime = os.path.join(AppRuntimeFolder, 'Scripts' , 'python.exe')

    

    Create_Shortcut(runtime , AppFolder, 'YouTube download.lnk' , f'"{mainapp}"', ico_path)
    
    shutil.rmtree(tempdirpath , ignore_errors=True)

__setup()