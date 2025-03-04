import doctest
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Абстрактный класс для транспортного средства."""

    def __init__(self, brand: str, speed: float, capacity: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства.
        :param speed: Скорость (в км/ч, должна быть положительной).
        :param capacity: Вместимость (должна быть положительным числом).

        Примеры:
        >>> v = Vehicle("Toyota", 100.0, 5)  # Должна быть ошибка, так как класс абстрактный
        Traceback (most recent call last):
            ...
        TypeError: Can't instantiate abstract class Vehicle with abstract method move
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом")

        self.brand = brand
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self) -> str:
        """Абстрактный метод для движения транспортного средства."""
        ...

    def get_info(self) -> str:
        """
        Получает информацию о транспортном средстве.

        :return: Строка с описанием.

        Примеры:
        >>> class Car(Vehicle):  # создаем подкласс для теста
        ...     def move(self): return "Машина едет"
        >>> c = Car("BMW", 150.0, 4)
        >>> c.get_info()
        'Транспортное средство: BMW, скорость: 150.0 км/ч, вместимость: 4 чел.'
        """
        return f"Транспортное средство: {self.brand}, скорость: {self.speed} км/ч, вместимость: {self.capacity} чел."


class Building(ABC):
    """Абстрактный класс для здания."""

    def __init__(self, address: str, floors: int, purpose: str) -> None:
        """
        Инициализация здания.

        :param address: Адрес здания.
        :param floors: Количество этажей (должно быть положительным числом).
        :param purpose: Назначение здания (например, "жилое" или "офисное").

        Примеры:
        >>> b = Building("ул. Ленина, 10", 5, "жилое")  # Ошибка, так как класс абстрактный
        Traceback (most recent call last):
            ...
        TypeError: Can't instantiate abstract class Building with abstract method get_building_type
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")
        if not isinstance(purpose, str):
            raise TypeError("Назначение должно быть строкой")

        self.address = address
        self.floors = floors
        self.purpose = purpose

    @abstractmethod
    def get_building_type(self) -> str:
        """Абстрактный метод для определения типа здания."""
        ...

    def get_info(self) -> str:
        """
        Получает информацию о здании.

        :return: Строка с описанием.

        Примеры:
        >>> class House(Building):  # создаем подкласс для теста
        ...     def get_building_type(self): return "Жилой дом"
        >>> h = House("ул. Пушкина, 20", 3, "жилое")
        >>> h.get_info()
        'Здание на ул. Пушкина, 20, этажей: 3, назначение: жилое'
        """
        return f"Здание на {self.address}, этажей: {self.floors}, назначение: {self.purpose}"


class SocialMedia(ABC):
    """Абстрактный класс для социальной сети."""

    def __init__(self, name: str, users_count: int, founded_year: int) -> None:
        """
        Инициализация социальной сети.

        :param name: Название соцсети.
        :param users_count: Количество пользователей (должно быть неотрицательным).
        :param founded_year: Год основания (должен быть в разумных пределах).

        Примеры:
        >>> sm = SocialMedia("FakeBook", 1000000, 2004)  # Ошибка, так как класс абстрактный
                Traceback (most recent call last):
                    ...
                TypeError: Can't instantiate abstract class SocialMedia with abstract method post_message
                """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(users_count, int) or users_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным числом")
        if not isinstance(founded_year, int) or founded_year < 1900 or founded_year > 2025:
            raise ValueError("Год основания должен быть разумным значением")

        self.name = name
        self.users_count = users_count
        self.founded_year = founded_year

    @abstractmethod
    def post_message(self, message: str) -> None:
        """Абстрактный метод для публикации сообщения."""
        ...

    def get_info(self) -> str:
        """
        Получает информацию о соцсети.

        :return: Строка с описанием.

        Примеры:
        >>> class Twitter(SocialMedia):  # создаем подкласс для теста
        ...     def post_message(self, message): return f"Опубликовано: {message}"
        >>> tw = Twitter("Twitter", 330000000, 2006)
        >>> tw.get_info()
        'Соцсеть Twitter, пользователей: 330000000, основана в 2006 году'
        """
        return f"Соцсеть {self.name}, пользователей: {self.users_count}, основана в {self.founded_year} году"

if __name__ == "__main__":
    doctest.testmod()