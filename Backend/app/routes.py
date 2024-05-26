from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.models import User
from datetime import datetime
from werkzeug.security import generate_password_hash
from app import db


api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('login') or not data.get('password'):
        return jsonify({'message': 'Логин и пароль обязательны.'}), 400

    login = data['login']
    password = data['password']

    user = User.query.filter_by(email=login).first()

    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Успешная аутентификация.'}), 200
    else:
        return jsonify({'message': 'Неверный логин или пароль.'}), 401
    
@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Нет данных для регистрации.'}), 400

    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    last_name = data.get('last_name')
    first_name = data.get('first_name')
    middle_name = data.get('middle_name')
    birth_date = data.get('birth_date')

    if not email or not password or not confirm_password or not last_name or not first_name or not birth_date:
        return jsonify({'message': 'Все поля обязательны для заполнения.'}), 400

    if password != confirm_password:
        return jsonify({'message': 'Пароли не совпадают.'}), 400

    # Проверка существования пользователя
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Пользователь с таким email уже существует.'}), 400

    # Хэширование пароля
    hashed_password = generate_password_hash(password)

    # Преобразование даты рождения в формат datetime
    try:
        birth_date = datetime.strptime(birth_date, '%d.%m.%Y').date()
    except ValueError:
        return jsonify({'message': 'Некорректный формат даты.'}), 400

    # Создание нового пользователя
    new_user = User(email=email, password=hashed_password, last_name=last_name, first_name=first_name, middle_name=middle_name, birth_date=birth_date)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Пользователь успешно зарегистрирован.'}), 201