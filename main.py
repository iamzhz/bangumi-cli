from parse_line import *
from call_other import *
from rich.console import Console
console = Console()
def main():
    line = ''
    
    print('Welcome to Ban-Terminal!\nType "help" for help.')
    while True:
        console.print('> ', style='green', end='')
        line = input()
        line_result = parse_line(line)
        call_other(line_result[0], line_result[1])
if __name__ == '__main__':
    main()