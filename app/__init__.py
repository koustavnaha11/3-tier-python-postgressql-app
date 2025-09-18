import os
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)

    db_user = os.getenv('DB_USER', 'myuser')
    db_password = os.getenv('DB_PASSWORD', 'mypassword')
    db_host = os.getenv('DB_HOST', 'mypgdb')  # IMPORTANT: Not localhost
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'mydatabase')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app
