#NOTE: Only works on windows-10

import os

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktopa').replace('\\' , '/')
try:
    f = open(f'{desktop}/desktop.ini' , 'r')
    f.close()
except FileNotFoundError:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Onedrive\\Desktop').replace('\\' , '/')



print(desktop)