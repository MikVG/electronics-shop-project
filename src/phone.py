from src.item import Item


class Phone(Item):
    """
    класс для представления телефона
    """

    def __init__(self, name, price, quantity, number_of_sim):
        """
        создание экземпляра класса Phone, который наследует поля из класса Item: name, price, quantity
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        геттер для приватного атрибута __number_of_sim класса Phone
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        сеттер для приватного атрибута __number_of_sim класа Phone, который проверяет, что количество
        сим-карт должно быть целым числом больше нуля.
        """
        if number_of_sim <= 0 or number_of_sim % 1 != 0:
            print("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков)
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """
        магический метод для отображения информации об объекте класса для пользователей
        """
        return f"{self.name}"

    def __add__(self, other):
        """
        метод для сложения экземплятор классов по количеству товаров, который выполняет проверку для сложения только
        экземпляров связанных классов
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None
