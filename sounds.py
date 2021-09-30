import simpleaudio as sa
import threading

def play(wav_path) -> None:
    wave_object = sa.WaveObject.from_wave_file(wav_path)
    play_object = wave_object.play()
    play_object.wait_done()

def button():
    """Button sound"""
    lolipop = threading.Thread(target=lambda:play('./assets/sounds/lever.wav'))
    lolipop.start()

def error():
    jellybean = threading.Thread(target=lambda:play('./assets/sounds/error.wav'))
    jellybean.start()

def ding():
    dong= threading.Thread(target=lambda:play('./assets/sounds/ding.wav'))
    dong.start()