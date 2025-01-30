import person.get
from the_path import the_path


def switch_to_person_by_person_id(person_id):
    status_code, content = person.get.get_person_by_person_id(person_id)
    if status_code == 400:
        print("[ERROR] Validation Error")
        return
    if status_code == 404:
        print("[ERROR] Not Found")
        return
    # status_code == 200
    the_path.set_path_des({
        'type': "person",
        'name': content['name'],
        'id': person_id,
        'more': content,
    })
