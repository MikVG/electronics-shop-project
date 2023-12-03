"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_name_len(item_class):
    item_class.name = 'СуперНоутбук'
    assert item_class.name == 'СуперНоутб'
    item_class.name = 'Ноутбук'
    assert item_class.name == 'Ноутбук'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(item_class):
    assert repr(item_class) == "Item('Ноутбук', 100000, 5)"

def test_str(item_class):
    assert str(item_class) == 'Ноутбук'

def test_add_quantity(item_class):
    phone = Phone('MyPhone', 50000, 7, 2)
    assert item_class + phone == 12

def test_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        Item.file = 'src/item.csv'
        Item.instantiate_from_csv()

def test_InstantiateCSVError():
    with pytest.raises(InstantiateCSVError):
        Item.file = 'src/items_test.csv'
        Item.instantiate_from_csv()
