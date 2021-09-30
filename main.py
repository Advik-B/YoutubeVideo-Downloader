from threading import Thread
from platform import system
from subprocess import run
from time import sleep
from sys import stdout
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

menu = f"""\n

--------------
| 1 | {menu_dict[1]} |
| 2 | {menu_dict[2]}   |
--------------
"""


while True:
    print('How do you want download your video?')
    print(menu)
    sel_meth = input('~~|: ')
    try:
        int_sel_meth = int(sel_meth)
        try:
            str_selmeth = menu_dict[int(sel_meth)]
        except KeyError:
            cls()
            print('Not a valid choice')
            continue
    except ValueError:
        try:
            str_selmeth = menu_dict2[sel_meth.casefold()]
        except KeyError:
            cls()
            print('Not a valid choice')
            continue
    print(f'You have selected: {str_selmeth}')
    if str_selmeth == 1 or str_selmeth.casefold() == 'search':
        print('line exec')
        sleep(1.5)
        cls()
        print('What is your search term?')
        search_term = input('~~|: ')
        cls()
        print('How many results do you want ?')
        try:
            results = int(input('~~|: '))
            if results >= 5:
                print(f'Are you shure you want THAT MANY RESULTS cause {results} vids will be downloaded [Y/N] ')
                confirmation = input('~~|: ')
                if confirmation.casefold() == 'y' or confirmation.casefold() == 'yes':
                    cls()
                    print('Ok. downloading vids ')
                    link_list=search(search_term , results=results)
                    cls()
                    found_vidnum = len(link_list)
                    if found_vidnum < results:
                        print('Found only', found_vidnum , 'vids')

                        if found_vidnum == 0:
                            cls()
                            print('NO RESULTS FOUND')
                            exit(0)
                        number_of_downloaded = 0
                        while number_of_downloaded <= found_vidnum:
                            number_of_downloaded += 1
                            print(f'Downloading video {number_of_downloaded} out of {found_vidnum}')
                            print()
                            print()
                            download_AV(link_list[number_of_downloaded - 1])
                            print('Done!')
                            sleep(.3)
            else:
                cls()
                print('Ok. downloading vids ')
                link_list=search(search_term , results=results)
                cls()
                found_vidnum = len(link_list)
                if found_vidnum == 0:
                    cls()
                    print('NO RESULTS FOUND')
                    exit(0)
                number_of_downloaded = 0
                while number_of_downloaded <= found_vidnum:
                    number_of_downloaded += 1
                    print(f'Downloading video {number_of_downloaded} out of {found_vidnum}')
                    print()
                    print()
                    download_AV(link_list[number_of_downloaded - 1])
                    print('Done!')
                    sleep(.3)



        except ValueError:
            print('Not a valid number')


    input('continew [PRESS ENTER]')



#NOTE: Work in progress 😅