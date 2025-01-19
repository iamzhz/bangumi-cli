from the_path import the_path
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
console = Console()


def show(args):
    if len(args) < 1:
        console.print("[red]TIP: [/red] please input something to show !")
        return
    func_dict = {
        "summary": show_summary,
        "tags": show_tags,
    }
    if args[0] in func_dict:
        func_dict[args[0]]()
    # it's no problem that a command is not found


def show_summary():
    summary = the_path.path_des['more']['summary']
    console.print(Panel(summary, title="Summary"))


def show_tags():
    original_tags = the_path.path_des['more']['tags']
    tags = [f"{i.get('name')}: [green]{i.get('count')}[/green]" for i in original_tags]
    console.print(Columns(tags, equal=True))
