import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """
        геттер для приватного атрибута __name класса Item
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        cеттер для приватного атрибута __name класса Item.
        Проверяет, что длина наименования товара (атрибут __name) не превышает 10 симвовов.
        В случае превышения, обрезает строку до первых 10 символов.
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def __repr__(self):
        """
        магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        магический метод для отображения информации об объекте класса для пользователей
        """
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        класс метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        absolutely_dir = os.path.dirname(__file__).replace('src', '')
        url = absolutely_dir + file
        with open(url, encoding='windows-1251') as f:
            csv_dict = csv.DictReader(f, delimiter=',')
            for text in csv_dict:
                name = text['name']
                price = cls.string_to_number(text['price'])
                quantity = cls.string_to_number(text['quantity'])
                item_csv = Item(name, price, quantity)
            return item_csv

    @staticmethod
    def string_to_number(string):
        """
        статический метод, возвращающий число из числа-строки
        """
        if string.isdigit():
            string = int(string)
        else:
            string = int(float(string))
        return string

    def __add__(self, other):
        """
        метод для сложения экземплятор классов по количеству товаров, который выполняет проверку для сложения только
        экземпляров связанных классов
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None
