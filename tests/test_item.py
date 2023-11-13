"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_class():
    return Item('Ноутбук', 100000, 5)


def test_class(item_class):
    assert item_class.name == 'Ноутбук'
    assert item_class.price == 100000
    assert item_class.quantity == 5


def test_calculate(item_class):
    assert item_class.calculate_total_price() == 500000


def test_discount(item_class):
    Item.pay_rate = 0.7
    item_class.apply_discount()
    assert item_class.price == 70000


def test_class_2():
    item_class_2 = Item('Телефон', 10000, 5)
    assert item_class_2.name == 'Телефон'
    assert item_class_2.price == 10000
    assert item_class_2.quantity == 5


def test_name_len():
    item_len = Item('Ноутбук', 100000, 5)
    item_len.name = 'СуперНоутбук'
    assert item_len.name == 'СуперНоутб'

