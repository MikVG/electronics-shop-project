"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


item = Item('Ноутбук', 100000, 5)
assert item.name == 'Ноутбук'
assert item.price == 100000
assert item.quantity == 5

assert item.calculate_total_price() == 500000

Item.pay_rate = 0.7
item.apply_discount()
assert item.price == 70000