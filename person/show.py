from the_path import the_path
import func.show_picture
from say_error import say_error
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
console = Console()


def show(args: list) -> None:
    if len(args) < 1:
        say_error.say("please input something to show !")
        return
    func_dict = {
        "summary": show_summary,
        "info": show_info,
        "id": show_id,
        "cover": show_cover,
        "photo": show_cover,
    }
    if args[0] in func_dict:
        func_dict[args[0]]()
    else:
        say_error.say(f"{args[0]} is not a valid option !")


def show_summary() -> None:
    summary = the_path.path_des['more']['summary']
    console.print(Panel(summary, title="Summary"))


def show_info() -> None:
    original_infobox = the_path.path_des['more']['infobox']  # string
    infobox = Table(title=the_path.path_des['name'])  # rich.table.Table
    infobox.add_column("Key", justify="right", style="cyan", no_wrap=True)
    infobox.add_column("Value", style="white")
    for i in original_infobox:
        value = i['value']
        if type(i['value']) is list:
            value = "\n".join(v['v'] for v in i['value'])
        infobox.add_row(i['key'], value)
    console.print(infobox)


def show_id() -> None:
    console.print(f"ID: {the_path.path_des['id']}")


def show_cover() -> None:
    image_url = the_path.path_des['more']['images']['small']
    func.show_picture.display_web_image(image_url)
