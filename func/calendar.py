import get_api
from rich.console import Console
from rich.table import Table
from datetime import datetime
def get_calendar():
    return get_api.get_api("/calendar")
def calendar(args):
    # deal with args
    if len(args) == 0:
        days = [datetime.now().weekday() + 1 ,]
    elif args[0] == "all":
        days = [1, 2, 3, 4, 5, 6, 7]
    else:
        days = []
        for i in args:
            if i.isdigit():
                days.append(int(i))
    # get from api
    _, cal = get_calendar()
    # print calendar
    for i in cal:
        if i['weekday']['id'] not in days:
            continue
        table = Table(title=f"Calendar {i['weekday']['en']}")
        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Chinese Name", style="magenta")
        for ii in i['items']:
            table.add_row(ii['name'], ii['name_cn'])
        console = Console()
        console.print(table)