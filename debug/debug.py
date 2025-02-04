from parse_line import parse_line
from call_other import call_other


def pre_run() -> None:
    """
    pre_run_list is a list of strings,
    each string is a command like "search xxx", "check xxxxxxx", "login" etc.
    pre_run_list = [
        "login",
        "search an_anime",
        "show tags"
    ]
    """
    pre_run_list = [
        "login",
        "search linkclick",
        "persons"
    ]
    for command in pre_run_list:
        print(f"--------- Run: `{command}` ----------")
        line_result = parse_line(command)
        call_other(line_result[0], line_result[1])
