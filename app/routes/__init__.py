from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth import auth
    from app.routes.jobs import jobs
    from app.routes.applications import applications
    from app.routes.admin import admin

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(jobs, url_prefix='/')
    app.register_blueprint(applications, url_prefix='/applications')
    app.register_blueprint(admin, url_prefix='/admin')

    return app