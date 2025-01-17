import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_class():
    return Phone('MyPhone', 50000, 7, 2)

def test_class(phone_class):
    assert phone_class.name == 'MyPhone'
    assert phone_class.price == 50000
    assert phone_class.quantity == 7

def test_add_quantity(phone_class):
    item = Item('Ноутбук', 100000, 5)
    assert item + phone_class == 12

def test_num_of_sim(phone_class):
    phone_class.number_of_sim = 0
    assert ("Количество физических SIM-карт должно быть целым числом больше нуля."
            == "Количество физических SIM-карт должно быть целым числом больше нуля.")
    phone_class.number_of_sim = 1.5
    assert ("Количество физических SIM-карт должно быть целым числом больше нуля."
            == "Количество физических SIM-карт должно быть целым числом больше нуля.")
