import get_api
from colorama import Fore, Back, Style
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
    print(f"{Fore.MAGENTA}Username{Style.RESET_ALL}: {info['username']}")
    print(f"{Fore.MAGENTA}Nickname{Style.RESET_ALL}: {info['nickname']}")
    print(f"{Fore.MAGENTA}Id{Style.RESET_ALL}: {info['id']}")
    print(f"{Fore.MAGENTA}Sign{Style.RESET_ALL}: {info['sign']}")
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