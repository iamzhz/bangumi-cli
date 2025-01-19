import func.help_info
import func.calendar
import account.user
import subject.search
import account.check
import account.login
from the_path import the_path
import os


def call_other(verb, args):
    func_dict = {
        "help": func.help_info.help_info,
        "cal": func.calendar.calendar,
        "user": account.user.user,
        "search": subject.search.search,
        "check": account.check.check_access_token,
        "login": account.login.login,
        "back": the_path.back_path_des,
        "exit": lambda args: exit(),
        "q": lambda args: exit(),
        "clear": lambda args: os.system('cls' if os.name == 'nt' else 'clear')
    }
    if verb in func_dict:
        func_dict[verb](args)
    elif verb is None:
        pass
    else:
        print("Invalid command")
