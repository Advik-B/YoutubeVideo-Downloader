from pafy import new
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