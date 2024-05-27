from models import *
from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS
from config import Config
from sqlalchemy.exc import NoResultFound
import re


import joblib

direction_names = {
    2: "Информатика и вычислительная техника",
    3: "Программная инженерия",
    4: "Информационная безопасность",
    5: "Биология",
    6: "Математика и математическое моделирование",
}


def predict_direction(model, label_encoder, subjects, direction_names):
    text_representation = " ".join(map(str, subjects))
    prediction_encoded = model.predict([text_representation])
    prediction_decoded = label_encoder.inverse_transform(prediction_encoded)
    predicted_direction = direction_names[prediction_decoded[0]]
    return predicted_direction


model = joblib.load("model.joblib")
label_encoder = joblib.load("label_encoder.joblib")


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
client = app.test_client()
app.config.from_object(Config)
engine = create_engine("sqlite:///db.sqlite")

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)

Base.metadata.create_all(bind=engine)


@app.route("/api/register", methods=["POST"])
def register():
    params = request.get_json()

    # Проверка наличия всех обязательных полей
    required_fields = [
        "email",
        "name",
        "middle_name",
        "last_name",
        "birth_date",
        "password",
    ]
    missing_fields = [
        field for field in required_fields if field not in params]
    if missing_fields:
        return jsonify({"error": f'Пропущенные поля: {", ".join(missing_fields)}'}), 400

    # Проверка формата email
    email_pattern = r"^\S+@\S+\.\S+$"
    if not re.match(email_pattern, params["email"]):
        return jsonify({"error": "Геправильный формат почты"}), 400

    # Проверка уникальности email
    existing_user = User.query.filter_by(email=params["email"]).first()
    if existing_user:
        return jsonify({"error": "Почта уже существует"}), 409

    try:
        # Создание нового пользователя
        user = User(**params)
        session.add(user)
        session.commit()

        # Генерация токена
        token = user.get_token()
        return jsonify({"token": token}), 201

    except IntegrityError:
        return jsonify({"error": "Сервер"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/login", methods=["POST"])
def login():
    try:
        params = request.get_json()
        user = User.authentificate(**params)
        token = user.get_token()
        return jsonify({"token": token})
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    except NoResultFound:
        return jsonify({"error": "Пользователь не найден"}), 404
    except Exception as e:
        return jsonify({"error": "Внутренняя ошибка сервера"}), 500


@app.route("/api/facultyselection", methods=["POST"])
def facultyselection():
    data = request.get_json()

    # Получение строки с названиями предметов из данных пользователя
    subjects_str = data["favorite_subjects"]

    # Преобразование строки с предметами в список, разделяя по запятой
    subjects_list = subjects_str.split(",")

    # Сопоставление каждого предмета с вашим словарем направлений
    favorite_subjects = [
        1 if subject.strip() in data["favorite_subjects"] else 0
        for subject in direction_names.values()
    ]

    # Прогнозирование направления с использованием вашей модели
    predicted_direction = predict_direction(
        model, label_encoder, favorite_subjects, direction_names
    )

    # Запись результата и данных пользователя в базу данных
    # faculty = FacultyForm(**data)
    # faculty.result = predicted_direction
    # session.add(faculty)
    # session.commit()

    return jsonify({"result": "predicted_direction"})


if __name__ == "__main__":
    app.run(debug=True)
