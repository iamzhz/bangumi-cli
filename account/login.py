from rich.console import Console
import func.check
console = Console()
access_token = None
def login():
    global access_token
    console.print("In order to login, you must provide your access token.")
    console.print("You can get your access token at [link=https://next.bgm.tv/demo/access-token]https://next.bgm.tv/demo/access-token[/link] .")
    access_token = input("Please enter your access token: ")
    if func.check.check_access_token([access_token]) == True:
        console.print("Login successful!")
        # TODO: save access token to file
    else:
        access_token = None
        console.print("Invalid access token. Please try again.")