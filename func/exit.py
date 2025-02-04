from rich.console import Console
console = Console()


def exit_program() -> None:
    console.print("\n[green]Goodbye![/green]\n")
    exit()


def signal_handler(signal, frame) -> None:
    exit_program()
