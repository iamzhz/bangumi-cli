import func.exit
import func.help_info
import func.calendar
import account.user
import subject.search
import subject.show
import account.check
import account.login
from the_path import the_path
import os


def call_other(verb, args):
    command_dict = {  # general commands
        "help": func.help_info.help_info,
        "cal": func.calendar.calendar,
        "user": account.user.user,
        "search": subject.search.search,
        "check": account.check.check_access_token,
        "login": account.login.login,
        "back": the_path.back_path_des,
        "exit": lambda args: func.exit.exit_program(),
        "q": lambda args: func.exit.exit_program(),
        "clear": lambda args: os.system('cls' if os.name == 'nt' else 'clear')
    }
    subject_command_dict = {  # subject commands
        "show": subject.show.show,
    }

    if 'type' in the_path.path_des:
        if the_path.path_des['type'] == 'subject' and verb in subject_command_dict:
            subject_command_dict[verb](args)
            return
    if verb in command_dict:
        command_dict[verb](args)
    elif verb is None:
        pass
    else:
        print("Invalid command")
