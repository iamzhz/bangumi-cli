import person.get
from the_path import the_path
import subject.subject
from say_error import say_error
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import get_api

console = Console()
SUBJECT_TYPE = {
    1: "Books",
    2: "Anime",
    3: "Music",
    4: "Game",
    6: "three-D",
}


def get_subject_person(args: list) -> None:
    # Check if in person page
    if the_path.path_des.get('type') != 'person':
        say_error.say("Not in person page")
        return
    # the_path.path_des['subjects'] is not exisiting, you must get it
    if 'subjects' not in the_path.path_des:
        status, subjects = person.get.get_person_related_subjects(the_path.path_des['id'])
        if status == 400:
            say_error.say("Validation Error")
            return
        elif status == 404:
            say_error.say("Not Found")
            return
        # elif status == 200:
        the_path.path_des['subjects'] = subjects
    # show the subjects
    subjects = the_path.path_des['subjects']
    subjects_table = Table(title=f"{the_path.path_des['name']} Subjects")
    subjects_table.add_column("Number", style="white")
    subjects_table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    subjects_table.add_column("Chinese Name", justify="right", style="yellow")
    subjects_table.add_column("Staff", style="white")
    subjects_table.add_column("Type", style="green")
    subject_count = 0
    for item in subjects:
        subjects_table.add_row(str(subject_count), item['name'], item['name_cn'], item['staff'], SUBJECT_TYPE[item['type']])
        subject_count += 1
    console.print(subjects_table)
    # ask to choose
    choices_list = [str(i) for i in range(-1, subject_count)]
    number = Prompt.ask('Please enter the number(-1 means `do not choose`): ', choices=choices_list, default='-1')
    number = int(number)  # str to int
    if number == (-1):
        return
    # switch to the subject
    subject.subject.switch_to_subject_by_subject_id(subjects[number]['id'])
