#NOTE: Only works on windows-10

from win32com.client import Dispatch
import os , winshell

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop').replace('\\' , '/')
try:
    f = open(f'{desktop}/desktop.ini' , 'r')
    f.close()
except FileNotFoundError:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Onedrive\\Desktop').replace('\\' , '/')

print(desktop) #TODO: Remove later

path = desktop.__add__('/Youtube_DL.lnk')  # Path to be saved (shortcut)
target = r"C:\Users\advik\Desktop\Harlem Shake (Original Army Edition).mp4"  # The shortcut target file or folder

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.save()