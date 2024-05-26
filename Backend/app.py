
from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
client = app.test_client()
app.config.from_object(Config)
engine = create_engine('sqlite:///db.sqlite')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)

from models import *

Base.metadata.create_all(bind=engine)

@app.route('/api/register', methods=['POST'])
def register():
    params = request.get_json()
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return jsonify({'token': token})

@app.route('/api/login', methods=['POST'])
def login():
    params = request.get_json()
    user = User.authentificate(**params)
    token = user.get_token()
    return jsonify({'token': token})

@app.route('/api/facultyselection', methods=['POST'])
def facultyselection():
    data = request.get_json()


    # Возьми значение из data и составь результат result
    # Записб в бд результата и дданных пользователя

    faculty = FacultyForm(**data)
    session.add(faculty)
    session.commit()

    result = "Результат"
    return jsonify({'facultyresult': "Результат"})

if __name__ == '__main__':
    app.run(debug=True)