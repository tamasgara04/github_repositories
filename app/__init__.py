from flask import Flask
from app.routes.repositories import repositories_blueprint
from app.utils.cache import cache
app = Flask(__name__)
cache.init_app(app)
app.register_blueprint(repositories_blueprint)
