import requests
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.style import Style
import math


def display_web_image(url, char_aspect_ratio=2.0):
    console = Console()
    try:
        # get image data from url
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        # get terminal size
        terminal_width, terminal_height = console.size
        # get image original size
        original_width, original_height = img.size
        image_ratio = original_width / original_height
        # calculate terminal aspect ratio
        terminal_ratio = terminal_width / (terminal_height * char_aspect_ratio)
        if image_ratio > terminal_ratio:
            # image is wider than terminal, scale by width
            new_width = terminal_width
            new_height = math.ceil(terminal_width / image_ratio / char_aspect_ratio)
        else:
            # image is taller than terminal, scale by height
            new_height = math.ceil(terminal_height * char_aspect_ratio)
            new_width = math.ceil(new_height * image_ratio)
        # resize image to fit terminal
        img = img.resize((math.ceil(new_width), math.ceil(new_height)), Image.NEAREST)
        # display image in terminal
        for y in range(new_height):
            for x in range(new_width):
                r, g, b = img.getpixel((x, y))[:3]
                color = Style(bgcolor=f"rgb({r},{g},{b})")
                console.print("  ", end="", style=color)
            console.print()  # new line

    except requests.RequestException as e:
        console.print(f"Error fetching image: {e}", style="bold red")
    except Exception as e:
        console.print(f"Error displaying image: {e}", style="bold red")
