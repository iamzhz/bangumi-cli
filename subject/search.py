import get_api
import subject.subject
from the_path import the_path
from say_error import say_error
from rich.console import Console
from rich.prompt import Prompt
console = Console()


def get_search_subjects(keyword: str, type: int = 2, responseGroup: str = 'small') -> (int, dict):
    return get_api.get_api(f'/search/subject/{keyword}?type={type}&responseGroup={responseGroup}')


def search(args: list) -> None:
    # check args length
    if len(args) == 0:
        say_error.say("Please enter a keyword to search.")
        return
    # call api
    keyword = args[0]
    status_code, result = get_search_subjects(keyword)
    # check status code
    if status_code is None:
        say_error.say(f"`[blue]{keyword}[/blue]` cannot be searched.")
        return
    # print result
    for count, i in enumerate(result['list']):
        console.print(f'[purple]{count}[/purple] [blue]|[/blue] {i["name"]}')
    # ask user to choose a subject
    choices_list = [str(i) for i in range(len(result['list']))]
    number = Prompt.ask('Please enter the number: ', choices=choices_list, default='0')
    console.print(f'You choose {result["list"][int(number)]["name"]}')
    # switch to subject page
    subject.subject.switch_to_subject_by_subject_id(result["list"][int(number)]['id'])
