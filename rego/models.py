from rego import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password_hash = db.Column(db.String)
    email = db.Column(db.String(254))

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
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254))
    contact_type_id = db.Column(
        db.Integer, db.ForeignKey('contact_type.it'), nullable=False
    )
                              
    contact_type = db.relationship(
        'ContactType',
        backref=db.backref('contacts', lazy=True)
    )

class ContactType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.String(1024), unique=True)
    data = db.Column(db.Text)

    
