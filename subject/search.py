import get_api
from subject.get import get_subject
from the_path import the_path
from rich.console import Console
from rich.prompt import Prompt
console = Console()
def get_search_subjects(keyword, type = 2, responseGroup = 'small'):
    return get_api.get_api(f'/search/subject/{keyword}?type={type}&responseGroup={responseGroup}')

def search(args):
    # check args length
    if len(args) == 0:
        print('Please enter a keyword to search.')
        return
    # call api
    keyword = args[0]
    status_code, result = get_search_subjects(keyword)
    # check status code
    if status_code is None:
        console.print(f'[bold red]Error[/bold red]: `[blue]{keyword}[/blue]` cannot be searched.')
        return
    # print result
    for count, i in enumerate(result['list']):
        console.print(f'[purple]{count}[/purple] [blue]|[/blue] {i["name"]}')
    # ask user to choose a subject
    choices_list = [str(i) for i in range(len(result['list']))]
    number = Prompt.ask('Please enter the number: ', choices=choices_list, default='0')
    console.print(f'You choose {result["list"][int(number)]["name"]}')
    # show information about the subject
    status_code, subject = get_subject(result['list'][int(number)]['id'])
    if status_code == 404:
        console.print('[bold red]Error[/bold red]: Subject not found.')
    if status_code == 401:
        console.print('[bold red]Error[/bold red]: Unauthorized.')
        return 
    # status_code == 200
    console.print(f'[bold green]Name[/bold green]: {subject["name"]}')
    console.print(f'[bold green]Chinese Name[/bold green]: {subject["name_cn"]}')
    console.print(f'[bold green]Summary[/bold green]: {subject["summary"]}')
    the_path.set_path_des([['subject', subject['name'], subject['id'], subject]])