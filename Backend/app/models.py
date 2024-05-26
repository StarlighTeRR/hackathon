from . import db
from werkzeug.security import generate_password_hash

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    birth_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
        }