# from __future__ import unicode_literals

# import os
# from django.core.files import File
# from .models import TitleError, ErrorCharacter
# from video_or_audio.models import Video, Audio
# from pytube import YouTube
# from youtube_dl import YoutubeDL
# from django.conf import settings


"""class YouTubeTiger:
    def __init__(self, url):
        self._title = ''
        self.filename = None
        self._url = url
        self._video_file = None
        self._audio_file = None
        self.video_details = {}
        self._download_options = {}
        self._video = None
        self._reference_video = None
        self._special_characters = None
        self._check_characters()

    def validate_link(self):
        valid = False

        try:

            with YoutubeDL(self._download_options) as ydl:
                self._video = ydl.extract_info(self._url, download=False)

            valid = True
        except:
            pass

        print(f'Valid link: {valid}\n')

        return valid"""


