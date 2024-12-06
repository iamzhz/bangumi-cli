import get_api
from rich.console import Console
console = Console()
def check_access_token(args):
    # check args
    if len(args) < 1:
        console.print('[bold red]Error[/bold red]: Please provide an access token.')
        return
    # check access token
    status_code, content = get_api.check_access_token(args[0])
    if status_code == 200:
        console.print(f'[bold green]Success[/bold green]: {content}')
    else:
        console.print(f'[bold red]{status_code}[/bold red]: {content}')
