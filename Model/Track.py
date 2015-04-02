from Global import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_imageattach.entity import Image, image_attachment


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    pub_year = db.Column(db.String(50))
    duration = db.Column(db.Integer) # in seconds
    type = db.Column(db.String(50))
    bitrate = db.Column(db.Integer) # in kbps
    file_url = db.Column(db.String(1000))
    genre = db.Column(db.String(50))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    # cover = image_attachment('Cover')

    artist = db.relationship('Artist', backref=db.backref('tracks', lazy='dynamic'))
    album = db.relationship('Album', backref=db.backref('tracks', lazy='dynamic'))

    __mapper_args__ = {
        'polymorphic_identity':'track',
        'polymorphic_on':type
    }

    def __init__(self, name=None,
                 year=None,
                 duration=None,
                 artist=None,
                 bitrate=None,
                 url=None,
                 album=None,
                 genre=None
                 ):
        self.name = name
        self.pub_year = year
        self.duration = duration
        self.artist = artist
        self.bitrate = bitrate
        self.file_url = url
        self.genre = genre

    def __repr__(self):
        return self.name