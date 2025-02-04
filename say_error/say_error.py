from rich.console import Console
console = Console()


def say(error_info: str, error_type: str = "") -> None:
    if error_type != "":
        error_type = f"({error_type})"
    console.print(f"[bold red]Error{error_type}[/bold red]: {error_info}")
