from pafy import new
try:
	from moviepy.editor import *
except ModuleNotFoundError as e: print(e)

import os

def download_aud(link:str) -> None:
	audio = new(link).getbestaudio(ftypestrict=False)
	audio.download()

def download_vid(link:str) -> None:
	video = new(link).getbestvideo(ftypestrict=False)
	video.download()

def download_AV(link:str) -> None:
	video = new(link)
	dl = video.getbest(ftypestrict=False)
	dl.download()

def download_thumb(link:str , outimage:str=None) -> None:
	import requests
	video = new(link)
	thumb  = (str(video.getbestthumb).split('Thumbnail: ')[1]).replace('>' , '').replace('default.jpg' , 'sddefault.jpg')
	r=requests.get(thumb ,allow_redirects=True , timeout=5)
	if outimage == None:
		outfilenum = 1
		while True:
			outfile = f'./thumb{outfilenum}.jpg'
			if os.path.isfile(outfile) or os.path.isdir(outfile):
				outfilenum += 1
				continue
			else:
				with open(outfile , 'wb') as img:
					img.write(r.content)
				break
	else:
		try:

			with open(outimage , 'wb') as img:
				img.write(r.content)
		except FileExistsError:
			pass

def getthumb(link:str) -> bytes:
	import requests
	video = new(link)
	thumb  = (str(video.getbestthumb).split('Thumbnail: ')[1]).replace('>' , '').replace('default.jpg' , 'sddefault.jpg')
	r=requests.get(thumb ,allow_redirects=True , timeout=5)
	return r.content

try:	
	def play_vid(path:str, name:str=None, fps:int=60 ) -> None:
			"""
			Play video:
			-
			- Will play the video with the given path

			Note:
			-
			- The windows title is by default set to the filename:\n
				ie:\n
				if the file name is `football.mp4`;\n
				then:\n
					the window title will be `football`\n
			
			- This function will also try to play the video in 60 FPS ( Frames-Per-Second )\n

			Optional:
			-
			- You can change the window title with `name` parameter
			- You can change the preffered FPS with `fps` parameter


			"""
			import pygame
			_path = path.replace('\\' , '/')
			__name = _path.split('/')[-1]
			_name = __name.split('.')[0]

			if name != None:
				pygame.display.set_caption(name)
			else:
				pygame.display.set_caption(_name)
			
			clip = VideoFileClip(path)
			clip.set_fps(fps)
			clip.preview()
			clip.close()
			pygame.quit()
except:
    pass