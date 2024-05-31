from rich import print
from rich._emoji_codes import EMOJI
from rich.color import ANSI_COLOR_NAMES
import random
from rich.prompt import Prompt, Confirm


def random_emoji(name):
    if available_emojies := [e for e in EMOJI if e[0] == name.lower()[0]]:
        return random.choice(available_emojies)
    else:
        return "t-rex"

def random_color():
    color = random.choice([color_name for color_name in ANSI_COLOR_NAMES.keys()])
    return color


def random_greeting(shout):
    greeting = random.choice(["Hi", "Bonjour", "Hallo", "Hej", "Terre"])
    if shout:
        greeting = greeting.upper()
    return greeting


def greet(name, shout):
    name = name.upper() if shout else name
    name_emoji = random_emoji(name=name)
    name_color = random_color()
    name_greeting = random_greeting(shout=shout)
    greeting = (
        f"{name_greeting} [bold {name_color}]{name}[/bold {name_color}] :{name_emoji}:"
    )
    print(greeting)


def main():
    name = Prompt.ask("Enter your name")
    shout = Confirm.ask("Shout?")
    greet(name=name, shout=shout)


if __name__ == "__main__":
    main()
