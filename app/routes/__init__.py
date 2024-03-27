from flask import jsonify
from .repositories import repositories_blueprint

@repositories_blueprint.errorhandler(Exception)
def handle_error(error):
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response
