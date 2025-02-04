import get_api


def get_subject(subject_id: any) -> (int, dict):
    # check login
    if not get_api.already_login():
        return 401, 'Unauthorized'
    # get subject
    return get_api.get_api(f'/v0/subjects/{subject_id}')
