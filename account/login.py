from rich.console import Console
from rich.prompt import Prompt
import os
import json
import account.check
console = Console()
access_token = None


def login():
    global access_token
    not_first_login = access_token is not None
    is_use_saved = 'n'
    # check if there is already an access token saved
    is_saved = os.path.exists('data/account.json')
    if is_saved:
        with open('data/account.json', 'r') as f:
            data = json.load(f)
            access_token = data['access_token']
        is_use_saved = Prompt.ask(f"Do you want to use the saved access token?({data['info']['username']})", choices=['y', 'n'], default='y')
        if is_use_saved == 'n':
            # delete info from saved file
            access_token = None
            data = None
            
    # output infomation
    if not is_saved and is_use_saved == 'n':
        console.print("In order to login, you must provide your access token.")
        console.print("You can get your access token at [link=https://next.bgm.tv/demo/access-token]https://next.bgm.tv/demo/access-token[/link] .")
        access_token = input("Please enter your access token: ")
    # check access token
    if account.check.check_access_token([access_token]) is True:
        console.print("Login successful!")
        if is_use_saved == 'n': # new enter access token
            is_save = Prompt.ask("Do you want to save your access token?", choices=['y', 'n'], default='y')
            if is_save == 'y':
                save_account_data(access_token)
    else:
        console.print("Invalid access token.")
        if not_first_login:
            will_be_saved = Prompt.ask("Still keep the last access token?", choices=['y', 'n'], default='y')
            if will_be_saved == 'n':
                access_token = None
            # will_be_saved == 'y': do not care, it is already


def write_dict_to_json(data, file_path):
    # make sure the directory exists
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # write data to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def save_account_data(access_token=access_token):
    data = {'access_token': access_token}
    data['info'] = account.user.get_user_info_me()[1]
    write_dict_to_json(data, 'data/account.json')
