from flask import Blueprint, request, jsonify
from app.services.github_service import GitHubService

repositories_blueprint = Blueprint('repositories', __name__)

@repositories_blueprint.route('/repositories/popular', methods=['GET'])
def get_popular_repositories():
    try:
        date = request.args.get('date')
        language = request.args.get('language')
        limit = request.args.get('limit')

        github_service = GitHubService()
        repositories = github_service.get_popular_repositories(date, language, limit)

        return jsonify(repositories)

    except Exception as e:
        raise Exception("Error retrieving popular repositories: " + str(e))
