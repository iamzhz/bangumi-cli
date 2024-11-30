import func.help_info
import func.calendar
import func.user
import func.search
import os
def call_other(verb, args):
    if verb == "help":
        func.help_info.help_info()
    elif verb == "cal":
        func.calendar.calendar()
    elif verb == "user":
        func.user.user(args)
    elif verb == "search":
        func.search.search(args)
    elif verb == "exit" or verb == "q":
        exit()
    elif verb == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif verb == None:
        pass
    else:
        print("Invalid command")