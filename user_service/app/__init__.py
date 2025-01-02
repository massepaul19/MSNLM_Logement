from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration de l'application
    app.config.from_object('config.Config')
    
    # Initialisation des extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Enregistrement des blueprints
    from app.routes import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    
    from app.admin_routes import admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/api/admin")

    # Route de base
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Bienvenue sur l'API !"}), 200

    return app
