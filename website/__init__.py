from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()



def create_app():
    app = Flask(__name__)

    ### App configuration ###
    app.config['SECRET_KEY'] = 'aP&8tM@xs8#1!C2f'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'database://username:password@host:port/databaseName'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    

    from .views import views
    from .auth import auth
    from .property_blueprint import property_bp

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(property_bp, url_prefix='/')

    from .models import User, Property, Interest 

    
    with app.app_context():
        db.create_all()  

    # Login manager configuration
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
