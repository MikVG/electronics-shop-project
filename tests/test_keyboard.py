import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard_class():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard(keyboard_class):
    assert keyboard_class.name == 'Dark Project KD87A'
    assert keyboard_class.price == 9600
    assert keyboard_class.quantity == 5
    assert keyboard_class.language == 'EN'

def test_change_lang(keyboard_class):
    keyboard_class.change_lang()
    assert (keyboard_class.language) == 'RU'
