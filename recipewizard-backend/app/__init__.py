from flask import Flask

from config import Config
from app.main import bp as main_bp
from app.recipes import bp as recipe_bp
from app.extensions import db, ma


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(recipe_bp, url_prefix="/recipes")

    @app.route("/test/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
