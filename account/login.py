from rich.console import Console
from rich.prompt import Prompt
import os
import json
import account.check
console = Console()
access_token = None


def login(args):
    global access_token
    not_first_login = access_token is not None
    is_use_saved = 'n'
    # check if there is already an access token saved
    is_saved = os.path.exists('data/account.json')
    is_get_from_file = False
    if is_saved:
        with open('data/account.json', 'r') as f:
            data = json.load(f)
        is_use_saved = Prompt.ask(f"Do you want to use the saved access token?({data['info']['username']})", choices=['y', 'n'], default='y')
    is_get_from_file = is_saved and is_use_saved == 'y'

    if is_get_from_file:
        access_token = data['access_token']
    else:  # not is_get_from_file
        console.print("In order to login, you must provide your access token.")
        console.print("You can get your access token at [link=https://next.bgm.tv/demo/access-token]https://next.bgm.tv/demo/access-token[/link] .")
        access_token = input("Please enter your access token: ")

    check_and_save_access_token(access_token, is_get_from_file)


def check_and_save_access_token(access_token, is_get_from_file):
    # check access token
    is_check_success, _ = account.check.check_access_token(access_token)
    if is_check_success:
        console.print("Login successful!")
        if not is_get_from_file:  # new enter access token
            is_save = Prompt.ask("Do you want to save your access token?", choices=['y', 'n'], default='y')
            if is_save == 'y':
                save_account_data(access_token)
    else:
        console.print("Invalid access token.")
        if is_get_from_file:
            is_need_delete = Prompt.ask("The saved access token is invalid. Do you want to delete it?", choices=['y', 'n'], default='n')
            if is_need_delete == 'y':
                os.remove('data/account.json')


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
