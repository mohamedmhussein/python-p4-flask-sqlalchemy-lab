from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    #The Zookeeper model should contain a name, a birthday, and a list of animals that they take care of.
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)
    animals = db.relationship('Animal', backref='zookeeper')

class Enclosure(db.Model):
    #The Enclosure model should contain an environment (grass, sand, or water), an open_to_visitors boolean, and a list of animals.
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean, default=True)
    animals = db.relationship('Animal', backref = 'enclosure')

class Animal(db.Model):
    #The Animal model should contain a name, a species, a zookeeper, and an enclosure.
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
