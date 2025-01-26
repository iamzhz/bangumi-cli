import get_api
from rich.console import Console
console = Console()


def check_access_token(access_token):
    """
    success: return True, content
    failure: return False, content
    """
    # check access token
    status_code, content = get_api.check_access_token(access_token)
    return status_code == 200, content


def show_check_access_token(args):
    # check args
    if len(args) < 1:
        console.print('[bold red]Error[/bold red]: Please provide an access token.')
        return
    # check access token
    is_success, content = check_access_token(args[0])
    if is_success:
        console.print(f'[bold green]Success[/bold green]: {content}')
        return True
    else:
        console.print(f'[bold red]Failure[/bold red]: {content}')
        return False
