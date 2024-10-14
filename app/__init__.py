from flask import Flask
from .config.config import Config
from .routes.views import bp 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp)
    
    with app.app_context():
        from .routes import views
        
    return app
