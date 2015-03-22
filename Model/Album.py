from Global import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    year = db.Column(db.DATETIME)
    duration = db.Column(db.Integer) # in seconds

    def __init__(self, name, year=None, duration=None):
        self.name = name
        self.year = year
        self.duration = duration

    def __repr__(self):
        return self.name