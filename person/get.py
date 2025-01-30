import get_api


def get_person_by_person_id(person_id):
    return get_api.get_api(f"/v0/persons/{person_id}")
