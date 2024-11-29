import func.help_info
import func.calendar
def call_other(verb, args):
    if verb == "help":
        func.help_info.help_info()
    elif verb == "cal":
        func.calendar.calendar()
    elif verb == "exit":
        exit()
    else:
        print("Invalid command")