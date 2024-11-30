import func.help_info
import func.calendar
import func.user
def call_other(verb, args):
    if verb == "help":
        func.help_info.help_info()
    elif verb == "cal":
        func.calendar.calendar()
    elif verb == "user":
        func.user.user(args)
    elif verb == "exit":
        exit()
    else:
        print("Invalid command")