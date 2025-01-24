from the_path import the_path
import get_api


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
    # TODO: do your things next time! you know.
        the_path.path_des['persons'] = persons
