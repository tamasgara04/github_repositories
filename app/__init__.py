from flask import Flask
from app.routes.repositories import repositories_blueprint

app = Flask(__name__)

app.register_blueprint(repositories_blueprint)
