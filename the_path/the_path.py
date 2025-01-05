path_cur = '/'
path_des = []
"""
a 'path_des' is a list of lists of two strings, an integer and a dict.
the first string is the type of the thing (subject, person, character, etc).
the second string is the name of the thing.
the integer is the id of the thing.
the dict is the additional information of the thing.
e.g.
path_des = [['subject', 'the_name', 320224, [A dict]]]
"""
def set_path_des(des):
    global path_des
    path_des = des
    
def des_to_path(des = path_des):
    global path_cur
    path_temp = ''
    for i in des:
        path_temp += f'[white]/[/white][on plum2]{i[0]}[/on plum2][white]-[/white][on light_slate_blue]{i[1]}[/on light_slate_blue]'
    if path_temp == '':
        path_temp = '[white]/[/white]'
    path_cur = path_temp