import pytest
import demo_app
from rich.color import Color


@pytest.mark.parametrize(
    "name",
    [
        "Marie Curie",
        "Alfred Nobel",
        "Charles Darwin",
        "Ada Lovelace",
        "Albert Einstein",
        "Jane Goodall",
    ],
)
def test_random_emoji(name):
    random_greeting = demo_app.random_emoji(name=name)
    expected_start = name[0].lower()
    assert random_greeting[0] == expected_start


def test_random_color():
    test_color = Color(name="TEST_COLOR", type=0)
    valid_color = test_color.parse(color=demo_app.random_color())
    assert valid_color


def test_greeting():
    greeting = demo_app.random_greeting(shout=False)
    assert greeting


def test_greeting_shout():
    greeting = demo_app.random_greeting(shout=True)
    assert greeting.isupper()


@pytest.mark.parametrize(
    "name,shout",
    [
        ("Marie Curie", True),
        ("Alfred Nobel", True),
        ("Charles Darwin", True),
        ("Ada Lovelace", True),
        ("Albert Einstein", True),
        ("Jane Goodall", True),
        ("Marie Curie", False),
        ("Alfred Nobel", False),
        ("Charles Darwin", False),
        ("Ada Lovelace", False),
        ("Albert Einstein", False),
        ("Jane Goodall", False),
    ],
)
def test_greet(name, shout, capsys):
    demo_app.greet(name=name, shout=shout)
    captured = capsys.readouterr()
    expected_name = name.upper() if shout else name
    assert expected_name in captured.out
