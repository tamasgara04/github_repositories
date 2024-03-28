import requests
from datetime import datetime
from app.utils.cache import cache

GITHUB_API_URL = "https://api.github.com/search/repositories"

class GitHubService:
    @cache.cached(timeout=60)
    def get_popular_repositories(self, date=None, language=None, limit=None):
        query_params = {
            'q': 'stars:>0',  # Retrieve repositories with at least 1 star
            'sort': 'stars',
            'order': 'desc'
        }

        if date:
            try:
                date = datetime.strptime(date, '%Y-%m-%d').date()
                query_params['q'] += f' created:>{date}'
            except ValueError:
                raise ValueError('Invalid date format. Please use YYYY-MM-DD.')

        if language:
            query_params['q'] += f' language:{language}'

        if limit:
            query_params['per_page'] = limit

        response = requests.get(GITHUB_API_URL, params=query_params)
        response.raise_for_status()  # Raise exception for non-2xx responses
        return response.json()['items']
