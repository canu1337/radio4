from sqlalchemy_imageattach.context import store_context
from Global import db
from Track import Track
import Tools
from Album import Album
from Artist import Artist
import os
import string
from flask import url_for
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen import File
from sqlalchemy_imageattach.entity import Store


class LocalTrack (Track):
    path = db.Column(db.String(1000))

    __mapper_args__ = {
        'polymorphic_identity': 'local_track',
    }

    def __init__(self, name=None,
                 year=None,
                 duration=None,
                 artist=None,
                 path=None,
                 bitrate=None,
                 url=None,
                 album=None,
                 genre=None
                 ):
        super(LocalTrack, self).__init__(name, year, duration, artist, album, bitrate, url, genre)
        self.path = path

    def __init__(self, path):
        audio = EasyID3(path)
        f = MP3(path)
        p = File(path)
        try:
            self.name = audio['title'][0]
        except KeyError:
            self.name = os.path.basename(os.path.splitext(audio.filename)[0])
        try:
            self.pub_year = audio['date'][0]
        except KeyError:
            pass
        try:
            self.artist = Tools.get_or_create(db.session, Artist, name=audio['artist'][0])
        except KeyError:
            pass
        try:
            self.path = path
        except KeyError:
            pass
        try:
            self.bitrate = f.info.bitrate / 1000
        except KeyError:
            pass
        try:
            self.album = Tools.get_or_create(db.session, Album, name=audio['album'][0])
        except KeyError:
            pass
        try:
            self.genre = audio['genre'][0]
        except KeyError:
            pass
        try:
            with store_context(store):
                self.cover.from_blob(image_binary)
        except:
            pass
        self.duration = f.info.length
        self.file_url = url_for('static', filename=path[string.rindex(path, 'library/'):])


