path_cur = '/'
des_stack = []
path_des = {}
"""
a 'path_des' is a dict of two strings, an integer and a dict.
the 'type' is a string of the type of the thing (subject, person, character, etc).
the 'name' is a string of the name of the thing.
the 'id' is an integer of the id of the thing.
the 'more' is a dict of the additional information of the thing.
other... (can be used by other functions when they need)
e.g.
path_des = {
'type': 'subject',
'name': 'the_name',
'id': 320224,
'more': {A dict}
}
"""


def set_path_des(des):
    global path_des
    path_des = des
    des_stack.append(des)


def back_path_des(args):
    global path_des, des_stack
    if len(des_stack) > 1:
        des_stack.pop()
        path_des = des_stack[-1]
    else:
        path_des = {}


def des_to_path(des=path_des):
    global path_cur
    path_temp = ''
    if des == {}:
        path_temp = '[white]/[/white]'
    else:
        path_temp += f'[white]/[/white][on plum2]{des["type"]}[/on plum2][white]-[/white][on light_slate_blue]{des["name"]}[/on light_slate_blue]'
    path_cur = path_temp
    return path_temp
