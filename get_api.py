import requests
import json
BASE_URL = "https://api.bgm.tv"
def get_api(relative_url):
    response = requests.get(BASE_URL + relative_url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

def get_calendar():
    return get_api("/calendar")