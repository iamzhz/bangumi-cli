import get_api
def calendar():
    cal = get_api.get_calendar()
    for i in cal[0]['items']:
        print(i['name'])