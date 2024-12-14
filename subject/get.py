import get_api
def get_subject(subject_id):
    # check login
    if get_api.already_login() == False:
        return 401, 'Unauthorized'
    # get subject
    return get_api.get_api(f'/v0/subjects/{subject_id}')