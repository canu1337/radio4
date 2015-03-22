from Global import db
from sqlalchemy_imageattach.entity import Image, image_attachment

class Cover(db.Model, Image):

    user_id = db.Column(db.Integer, db.ForeignKey('Track.id'), primary_key=True)
    user = db.relationship('Track')