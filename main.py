from moviepy.editor import *

convVideo = input("Please insert the video source.\n")

def convert(videoSource):
    mp3 = "Converted.mp3"
    mp4 = videoSource
    video = VideoFileClip(mp4)
    audio = video.audio
    audio.write_audiofile(mp3)

convert(convVideo)