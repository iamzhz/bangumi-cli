import get_api
from say_error import say_error
import func.show_picture
from rich.table import Table
from rich.console import Console
console = Console()


def get_user_info_by_name(username: str) -> (int, dict):
    return get_api.get_api(f"/v0/users/{username}")


def get_user_info_me() -> (int, dict):
    return get_api.get_api("/v0/me")


def output_user_info_by_dict(info: dict) -> None:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Key", style="dim", width=12)
    table.add_column("Value")
    table.add_row("Username", info['username'])
    table.add_row("Nickname", info['nickname'])
    table.add_row("Id", str(info['id']))
    table.add_row("Sign", info['sign'])
    console.print(table)


def user_info(args: list) -> None:
    if len(args) == 0:
        say_error.say("Please enter the username.")
        return
    status, info = get_user_info_by_name(args[0])
    if status == 400:
        say_error.say("Username too long.")
        return
    if status == 404:
        say_error.say("User not found.")
        return
    # status == 200
    output_user_info_by_dict(info)


def user_avatar(args: list) -> None:
    if len(args) == 0:
        say_error.say("Please enter the username.")
        return
    status, info = get_user_info_by_name(args[0])
    if status == 400:
        say_error.say("Username too long.")
        return
    if status == 404:
        say_error.say("User not found.")
        return
    # status == 200
    func.show_picture.display_web_image(info['avatar']['small'])


def user_info_me() -> bool:
    status, info = get_user_info_me()
    if status == 401:
        say_error.say("Unauthorized.")
        return False
    if status == 200:
        output_user_info_by_dict(info)
        return True
    return False


def user(args: list) -> None:
    if len(args) == 0:
        say_error.say("Please enter the args.")
        return
    if args[0] == 'info':
        user_info(args[1:])
    elif args[0] == 'me':
        return user_info_me()
    elif args[0] == 'avatar':
        user_avatar(args[1:])
        pass
    else:
        say_error.say("Invalid args.")
