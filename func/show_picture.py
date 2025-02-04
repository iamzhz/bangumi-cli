from say_error import say_error
import requests
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.style import Style


def display_web_image(url: str, char_aspect_ratio: float = 2.0, scale_factor: float = 0.8) -> None:
    console = Console()
    try:
        # Get image data from URL
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))

        # Get terminal size
        terminal_width, terminal_height = console.size
        # print(f"Terminal size: {terminal_width}x{terminal_height}")

        # Get image original size
        original_width, original_height = img.size
        # print(f"Original image size: {original_width}x{original_height}")

        # Calculate image and terminal aspect ratios
        image_ratio = original_width / original_height
        terminal_ratio = terminal_width / (terminal_height * char_aspect_ratio)

        # Calculate new dimensions
        if image_ratio > terminal_ratio:
            # Image is wider than terminal, scale by width
            new_width = terminal_width * scale_factor
            new_height = (terminal_width * scale_factor) / image_ratio / char_aspect_ratio
        else:
            # Image is taller than terminal, scale by height
            new_height = terminal_height * char_aspect_ratio * scale_factor
            new_width = new_height * image_ratio

        # Ensure new dimensions do not exceed terminal size
        new_width = min(new_width, terminal_width)
        new_height = min(new_height, terminal_height * char_aspect_ratio)

        # Round dimensions to integers
        new_width = int(new_width)
        new_height = int(new_height)
        # print(f"New image size: {new_width}x{new_height}")

        # Resize image
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Display image in terminal
        for y in range(new_height):
            for x in range(new_width):
                r, g, b = img.getpixel((x, y))[:3]
                color = Style(bgcolor=f"rgb({r},{g},{b})")
                console.print("  ", end="", style=color)
            console.print()  # New line

    except requests.RequestException as e:
        say_error.say(f"Error fetching image: {e}")
    except Exception as e:
        say_error.say(f"Error displaying image: {e}")
