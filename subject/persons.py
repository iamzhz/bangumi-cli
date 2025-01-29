from the_path import the_path
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import get_api

console = Console()


def get_subject_person(args):
    # Check if in subject page
    if the_path.path_des.get('type') != 'subject':
        print("Not in subject page")
        return
    # the_path.path_des['persons'] is not exisiting, you must get it
    if 'persons' not in the_path.path_des:
        status, persons = get_api.get_api(f"/v0/subjects/{the_path.path_des.get('id')}/persons")
        if status == 400:
            print("Validation Error")
            return
        elif status == 404:
            print("Not Found")
            return
        # elif status == 200:
        the_path.path_des['persons'] = persons
    # show the persons
    persons_table = Table(title=f"{the_path.path_des['name']} Persons")
    persons_table.add_column("Number", style="white")
    persons_table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    persons_table.add_column("Relation", style="white")
    person_count = 0
    for person in the_path.path_des['persons']:
        persons_table.add_row(str(person_count), person['name'], person['relation'])
        person_count += 1
    console.print(persons_table)
    # ask to choose
    choices_list = [str(i) for i in range(-1, person_count)]
    number = Prompt.ask('Please enter the number(-1 means `do not choose`): ', choices=choices_list, default='-1')
    if number == "-1":
        return
    # TODO: to display the detailed info
