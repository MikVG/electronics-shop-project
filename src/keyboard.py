from src.item import Item


class MixinLang:
    """
    Миксин класс для добавления языка и измерения языка клавиатуры
    """

    def __init__(self):
        """
        метод инициализации класса
        """
        self.__language = 'EN'

    @property
    def language(self):
        """
        геттер для приватного атрибута __language
        """
        return self.__language

    def change_lang(self):
        """
        метод для изменения языка клавиатуры
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для описания клавиатуры, наследуется из класса Item и MixinLang
    """

    def __init__(self, name, price, quantity):
        """
        Метод для инициализации класса
        """
        super().__init__(name, price, quantity)
