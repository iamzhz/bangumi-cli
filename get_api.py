import requests
import json
BASE_URL = "https://api.bgm.tv"
headers = {'User-Agent': 'iamzhz/ban-terminal (https://github.com/iamzhz/ban-terminal)'}
def get_api(relative_url):
    response = requests.get(BASE_URL + relative_url, headers=headers)
    return response.status_code, json.loads(response.text)

def get_calendar():
    return get_api("/calendar")
def get_user_info_by_name(username):
    return get_api(f"/v0/users/{username}")
def get_search_subjects(keyword, type = 2, responseGroup = "small"):
    return get_api(f"/search/subject/{keyword}?type={type}&responseGroup={responseGroup}")