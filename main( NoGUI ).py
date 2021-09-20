from functions import *
from search import *
from threading import *
from sounds import *
from PIL import Image
def cls():
    os.system('cls')

def clear():
    cls()

def Download_video():
    cls()
    button()
    print('What do you want to search for?\n')
    query = input('  -: ')
    link_list = search(query)[0]
    download_thumb(link_list)
    im = Image.open("./thumb1.jpg") 
    im.show()
    download_AV(link_list)
    play_vid(r'E:\GIthub repos\YoutubeVideo-Downloader\I Cheated with SECURITY CAMERAS in a Building Competition....mp4')

Download_video()