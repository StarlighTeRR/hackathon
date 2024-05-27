from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

Base = declarative_base()

engine = create_engine("sqlite:///db.sqlite")
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = session.query_property()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    last_name = Column(String(120), nullable=False)
    middle_name = Column(String(120), nullable=True)
    birth_date = Column(String(120), nullable=False)

    def __init__(self, email, name, last_name, middle_name, birth_date, password):
        self.email = email
        self.name = name
        self.password = bcrypt.hash(password)
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date

    def get_token(self, expire_time=24):
        expire_delta = timedelta(hours=expire_time)
        token = create_access_token(identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod    
    def authentificate(cls, email, password):
        user = cls.query.filter_by(email=email).one_or_none()
        if user is None:
            raise ValueError("Пользователь не найден")
        if not bcrypt.verify(password, user.password):
            raise ValueError("Неверный пароль")
        return user

class FacultyForm(Base):
    __tablename__ = "faculty_forms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    favorite_subjects = Column(String(100), nullable=False)
    result = Column(String(120), nullable=False)

    def __init__(self, favorite_subjects, result):
        self.favorite_subjects = favorite_subjects
        self.result = result

Base.metadata.create_all(bind=engine)