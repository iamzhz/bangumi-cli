import get_api
from rich.console import Console
console = Console()
def user_info(args):
    if len(args) == 0:
        print("Please enter the username.")
        return
    status, info = get_api.get_user_info_by_name(args[0])
    if status == 400:
        print('Username too long.')
        return
    if status == 404:
        print('User not found.')
        return
    # status == 200
    console.print(f"[u]Username[/u]: {info['username']}")
    console.print(f"[u]Nickname[/u]: {info['nickname']}")
    console.print(f"[u]Id[/u]: {info['id']}")
    console.print(f"[u]Sign[/u]: {info['sign']}")
def user(args):
    if len(args) == 0:
        print("Please enter the args.")
        return
    if args[0] == 'info':
        user_info(args[1:])
    elif args[0] == 'avatar':
        # TODO
        pass
    else:
        print("Invalid args.")