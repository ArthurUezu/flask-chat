from app import db
from datetime import datetime

class Message(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    message=db.Column(db.Text, nullable=False)
    color=db.Column(db.String(7), nullable=True)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

