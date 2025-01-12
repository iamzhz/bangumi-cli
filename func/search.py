import get_api
from rich.console import Console
from rich.prompt import Prompt
console = Console()


def get_search_subjects(keyword, type=2, responseGroup="small"):
    return get_api.get_api(f"/search/subject/{keyword}?type={type}&responseGroup={responseGroup}")


def search(args):
    # check args length
    if len(args) == 0:
        print("Please enter a keyword to search.")
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
    # TODO: add more information about the subject
