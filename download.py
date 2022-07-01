from pytube import Playlist
from moviepy.editor import *
import glob
import os


class Download:

    def playlist(self, url, mp3=False, mp4=False):
        yt = Playlist(url)
        for video in yt.videos:
            video.streams.filter(progressive=True, file_extension='mp4').order_by(
                'resolution').desc().first().download()
        if mp3:
            lista_mp4 = glob.glob('*.mp4')
            for video in lista_mp4:
                mp4 = VideoFileClip(os.path.join(video))
                nome_mp3 = video[:-4] + '.mp3'
                mp4.audio.write_audiofile(os.path.join(nome_mp3))

        if mp4:
            lista_mp4 = glob.glob('*.mp4')
            for video in lista_mp4:
                os.remove(video)