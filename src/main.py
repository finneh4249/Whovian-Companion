#main code file 
import os

from flask import Flask

from controllers.cli_controllers import db_commands
from controllers.auth_controllers import auth_bp


from init import db, ma, bcrypt, jwt

# Application factories

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)   
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_bp)
    
    return app


