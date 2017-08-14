from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    comment = db.Column(db.String(300), unique=True)
