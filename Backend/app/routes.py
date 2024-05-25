from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.models import User

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