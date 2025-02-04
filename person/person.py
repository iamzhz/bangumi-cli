import person.get
from say_error import say_error
from the_path import the_path


def switch_to_person_by_person_id(person_id: any) -> None:
    status_code, content = person.get.get_person_by_person_id(person_id)
    if status_code == 400:
        say_error.say("Validation Error")
        return
    if status_code == 404:
        say_error.say("Not Found")
        return
    # status_code == 200
    the_path.set_path_des({
        'type': "person",
        'name': content['name'],
        'id': person_id,
        'more': content,
    })
