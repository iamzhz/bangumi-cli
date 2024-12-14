from rich.console import Console
from rich.prompt import Prompt
import account.check
console = Console()
access_token = None
def login():
    global access_token
    not_first_login = access_token is not None
    # output infomation
    console.print("In order to login, you must provide your access token.")
    console.print("You can get your access token at [link=https://next.bgm.tv/demo/access-token]https://next.bgm.tv/demo/access-token[/link] .")
    access_token = input("Please enter your access token: ")
    # check access token
    if account.check.check_access_token([access_token]) == True:
        console.print("Login successful!")
        # TODO: save access token to file
    else:
        console.print("Invalid access token.")
        if not_first_login:
            will_be_saved = Prompt.ask("Still keep the last access token?", choices=['y', 'n'], default='y')
            if will_be_saved == 'n':
                access_token = None
            # will_be_saved == 'y': do not care, it is already