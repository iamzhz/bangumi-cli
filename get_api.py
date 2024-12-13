import requests
import json
import account.login
BASE_URL = "https://api.bgm.tv"
headers = {
    'User-Agent': 'iamzhz/ban-terminal (https://github.com/iamzhz/ban-terminal)',
    #'Authorization': f'Bearer {account.login.access_token}'
}
def get_api(relative_url):
    # refresh access_token
    if account.login.access_token is not None:
        headers['Authorization'] = f'Bearer {account.login.access_token}'
    # get api
    try:
        response = requests.get(BASE_URL + relative_url, headers=headers)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return None, str(e)  # Request Error



def check_access_token(access_token):
    url = 'https://bgm.tv/oauth/token_status'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'iamzhz/ban-terminal (https://github.com/iamzhz/ban-terminal)'
    }
    data = {
        "access_token": access_token
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return 200, response.json()
        else:
            return response.status_code, "Error"
    except requests.exceptions.RequestException as e:
        return None, e  # Request Error
    return None