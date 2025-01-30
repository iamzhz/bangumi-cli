import func.exit
import help_info.help_info
import cal.cal
import account.user
import subject.search
import subject.show
import account.check
import account.login
import subject.persons
import person.show
from the_path import the_path
import os


def call_other(verb, args):
    command_dict = {  # general commands
        "help": help_info.help_info.help_info,
        "cal": cal.cal.calendar,
        "user": account.user.user,
        "search": subject.search.search,
        "check": account.check.show_check_access_token,
        "login": account.login.login,
        "back": the_path.back_path_des,
        "exit": lambda args: func.exit.exit_program(),
        "q": lambda args: func.exit.exit_program(),
        "clear": lambda args: os.system('cls' if os.name == 'nt' else 'clear'),
    }
    subject_command_dict = {  # subject commands
        "show": subject.show.show,
        "persons": subject.persons.get_subject_person,
    }
    person_command_dict = {
        "show": person.show.show,
    }

    the_path_type = the_path.path_des.get('type')
    if the_path_type == 'subject' and verb in subject_command_dict:
        subject_command_dict[verb](args)
        return
    if the_path_type == 'person' and verb in person_command_dict:
        person_command_dict[verb](args)
        return
    if verb in command_dict:
        command_dict[verb](args)
    elif verb is None:
        pass
    else:
        print("Invalid command")
