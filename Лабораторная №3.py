class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Имя книги (только для чтения)."""
        return self._name

    @property
    def author(self) -> str:
        """Автор книги (только для чтения)."""
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги с количеством страниц."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # будет использован сеттер ниже

    @property
    def pages(self) -> int:
        """Количество страниц (целое число, больше 0)."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self) -> str:
        # Перегружаем str, чтобы добавить информацию о страницах
        return f"{super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"pages={self.pages})")


class AudioBook(Book):
    """Класс для аудиокниги с длительностью."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # будет использован сеттер ниже

    @property
    def duration(self) -> float:
        """Длительность аудиокниги (число с плавающей точкой, больше 0)."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Длительность должна быть числом (float или int)")
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = float(value)

    def __str__(self) -> str:
        # Перегружаем str, чтобы добавить информацию о длительности
        return f"{super().__str__()}. Продолжительность: {self.duration} ч."

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"duration={self.duration})")