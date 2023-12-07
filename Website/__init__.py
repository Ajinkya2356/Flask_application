from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "a234drwer" #provide secret key of your choice
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Mwerxz23@localhost/User" #provide your username and password
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    db.init_app(app)
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    from .models import Users

    with app.app_context():
        db.create_all()
   
    

    return app
