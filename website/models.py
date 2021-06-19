from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""
Definire la classe che identidica un Referendum, inserendovi:
id di colonna, la domanda, la prima e la seconda risposta 
possibili, i voti che hanno ricevuto, chi ha votato già, l'id
dell'utente che possiede il ref
"""
class Refs(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question = db.Column(db.String(200))
    fAnsw = db.Column(db.String(200))
    sAnsw = db.Column(db.String(200))
    fVote = db.Column(db.Integer, default=0)
    sVote = db.Column(db.Integer, default=0)
    voters = db.Column(db.String(10000), default="")
    user_name = db.Column(db.String(200), db.ForeignKey('user.name'))

"""
Definire la classe utente inserendo il suo nome, la sua 
password, e tutti i Referendum da lui creato
"""
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    refs = db.relationship('Refs')
