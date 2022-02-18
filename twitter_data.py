"""Get data about user from Twitter"""
import requests
import hidden


def get_data(nickname: str) -> dict:
    """
    Get data about user from Twitter and return it as a dictionary.
    """
    base_url = "https://api.twitter.com/"
    bearer_token = hidden.token()
    search_url = f'{base_url}1.1/friends/list.json'
    search_headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    search_params = {
        'screen_name': '@',
        'count': 2
    }
    search_params['screen_name'] = f'@{nickname}'
    response = requests.get(
        search_url, headers=search_headers, params=search_params)
    data = response.json()
    return data
