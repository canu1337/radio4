from Global import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    year = db.Column(db.DATETIME)
    duration = db.Column(db.Integer) # in seconds
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    artist = db.relationship('Artist', backref=db.backref('albums', lazy='dynamic'))

    def __init__(self, name, year=None, duration=None):
        self.name = name
        self.year = year
        self.duration = duration

    def __repr__(self):
        return self.name