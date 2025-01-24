from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def help_info(args):
    console = Console()

    help_text = Text('Welcome to Bangumi-CLI help information!\n\n')

    # General Commands
    help_text.append('General Commands:\n', style='bold')
    help_text.append('  - help: Show this help information.\n')
    help_text.append('  - exit / q: Exit the program.\n')
    help_text.append('  - clear: Clear the screen.\n\n')

    # User-related Commands
    help_text.append('User-related Commands:\n', style='bold')
    help_text.append('  - user info {username}: View the user information of the specified username.\n')
    help_text.append('  - user me: View the information of the currently logged-in user.\n')
    help_text.append('  - user avatar {username}: View the avatar of the specified username.\n\n')

    # Subject-related Commands
    help_text.append('Subject-related Commands:\n', style='bold')
    help_text.append('  - search: Search for subjects.\n')
    help_text.append('  - show: Display relevant information about the subject, supporting the following sub-commands:\n')
    help_text.append('    - summary: Display the subject summary.\n')
    help_text.append('    - tags: Display the subject tags.\n')
    help_text.append('    - info: Display detailed information about the subject.\n')
    help_text.append('    - collection: Display the subject collection information.\n')
    help_text.append('    - id: Display the subject ID.\n')
    help_text.append('    - cover: Display the subject cover.\n\n')

    # Other Commands
    help_text.append('Other Commands:\n', style='bold')
    help_text.append('  - cal: View the calendar.\n')
    help_text.append('  - check: Check the access token.\n')
    help_text.append('  - login: Log in.\n')
    help_text.append('  - back: Return to the previous path.\n\n')

    help_text.append('More features will be added in the future.')

    panel = Panel(help_text, title="Bangumi-CLI Help", border_style="blue")
    console.print(panel)
