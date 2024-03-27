from ..app.services.github_service import GitHubService

def test_get_popular_repositories():
    github_service = GitHubService()
    repositories = github_service.get_popular_repositories()
    assert isinstance(repositories, list)
