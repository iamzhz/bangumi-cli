import get_api
from rich.console import Console
from rich.prompt import Prompt
console = Console()
def search(args):
    if len(args) == 0:
        print("Please enter a keyword to search.")
        return
    keyword = args[0]
    _, result = get_api.get_search_subjects(keyword)
    
    for count, i in enumerate(result['list']):
        console.print(f'[purple]{count}[/purple] [blue]|[/blue] {i["name"]}')
    choices_list = [str(i) for i in range(len(result['list']))]
    number = Prompt.ask('Please enter the number: ', choices=choices_list, default='0')
    console.print(f'You choose {result["list"][int(number)]["name"]}')
    # TODO: add more information about the subject