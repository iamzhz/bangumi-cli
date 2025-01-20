from the_path import the_path
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
console = Console()


def show(args):
    if len(args) < 1:
        console.print("[red]TIP: [/red] please input something to show !")
        return
    func_dict = {
        "summary": show_summary,
        "tags": show_tags,
        "info": show_info,
    }
    if args[0] in func_dict:
        func_dict[args[0]]()
    else:
        console.print(f"[red]TIP: [/red] {args[0]} is not a valid option !")


def show_summary():
    summary = the_path.path_des['more']['summary']
    console.print(Panel(summary, title="Summary"))


def show_tags():
    original_tags = the_path.path_des['more']['tags']
    tags = [f"{i.get('name')}: [green]{i.get('count')}[/green]" for i in original_tags]
    console.print(Columns(tags, equal=True))


def show_info():
    original_infobox = the_path.path_des['more']['infobox']
    infobox = Table(title=the_path.path_des['name'])
    infobox.add_column("Key", justify="right", style="cyan", no_wrap=True)
    infobox.add_column("Value", style="magenta")
    for i in original_infobox:
        value = i['value']
        if type(i['value']) is list:
            value = "\n".join(v['v'] for v in i['value'])
        infobox.add_row(i['key'], value)
    console.print(infobox)
