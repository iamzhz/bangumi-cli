import func.help_info
import func.calendar
import account.user
import func.search
import account.check
import account.login
import os
def call_other(verb, args):
    if verb == "help":
        func.help_info.help_info()
    elif verb == "cal":
        func.calendar.calendar(args)
    elif verb == "user":
        account.user.user(args)
    elif verb == "search":
        func.search.search(args)
    elif verb == "check":
        account.check.check_access_token(args)
    elif verb == "login":
        account.login.login()
    elif verb == "exit" or verb == "q":
        exit()
    elif verb == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif verb == None:
        pass
    else:
        print("Invalid command")