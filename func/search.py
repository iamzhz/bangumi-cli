import get_api
def search(args):
    if len(args) == 0:
        print("Please enter a keyword to search.")
        return
    keyword = args[0]
    _, result = get_api.get_search_subjects(keyword)
    for i in result['list']:
        print(i['name'])