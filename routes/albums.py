from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
ß
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Album(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    tracks = db.Column(db.PickleType, nullable=True)

class Artist(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genres = db.Column(db.PickleType, nullable=True)

class Playlist(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    public = db.Column(db.Boolean, nullable=False)
    tracks = db.Column(db.PickleType, nullable=True)
