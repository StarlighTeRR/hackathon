from app import db, session, Base
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    birth_date = db.Column(db.String(120), nullable=False)

    def __init__(self, email,name,last_name,middle_name,birth_date,password):
        self.email = email
        self.name = name
        self.password = bcrypt.hash(password)
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authentificate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            return "Неверный пароль"
        return user
    
class FacultyForm(Base):
    __tablename__ = 'faculty_forms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    favorite_subjects = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(120), nullable=False)

    def __init__(self, favorite_subjects,result):
        self.favorite_subjects = favorite_subjects
        self.result = result



