from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password_hash = db.Column(db.String)
    email = db.Column(db.String)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class OrgAdmin(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, primary_key=True)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Contact(db.Model):
    pass

class ContactType(db.Model):
    pass

class Entity(db.Model):
    pass
