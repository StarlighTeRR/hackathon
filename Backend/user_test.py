from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Создайте пользователя
    new_user = User(email='test1@example.com', password=generate_password_hash('password'))
    db.session.add(new_user)
    db.session.commit()
    print("Пользователь успешно добавлен")