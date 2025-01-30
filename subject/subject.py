from the_path import the_path
import subject.get
from rich.console import Console

console = Console()


def switch_to_subject_by_subject_id(subject_id):
    status_code, content = subject.get.get_subject(subject_id)
    if status_code == 404:
        console.print('[bold red]Error[/bold red]: Subject not found.')
    if status_code == 401:
        console.print('[bold red]Error[/bold red]: Unauthorized.')
        return
    # status_code == 200
    the_path.set_path_des({
        'type': 'subject',
        'name': content['name'],
        'id': content['id'],
        'more': content
    })
