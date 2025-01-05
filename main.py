from the_path import the_path
from parse_line import *
from call_other import *
from rich.console import Console
console = Console()
def main():
    line = ''

    print('Welcome to Bangumi-CLI!\nType "help" for help.')
    while True:
        the_path.des_to_path(the_path.path_des)
        console.print(f'[black]{the_path.path_cur}[/black]> ', style='green', end='')
        line = input()
        line_result = parse_line(line)
        call_other(line_result[0], line_result[1])
if __name__ == '__main__':
    main()