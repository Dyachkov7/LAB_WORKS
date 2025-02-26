from typing import Any


class InputDevice:
    """
    Базовый класс для устройств ввода.
    """

    def __init__(self, brand: str, model: str, wireless: bool) -> None:
        """
        Инициализирует устройство ввода.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param wireless: Флаг беспроводного соединения.
        """
        self.brand = brand
        self.model = model
        self.wireless = wireless

    def __str__(self) -> str:
        """
        Возвращает строковое представление устройства.
        """
        return f"{self.brand} {self.model} ({'Wireless' if self.wireless else 'Wired'})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"InputDevice(brand={self.brand!r}, model={self.model!r}, wireless={self.wireless!r})"

    def connect(self) -> str:
        """
        Метод подключения устройства.
        """
        return f"{self.brand} {self.model} подключено."


class Keyboard(InputDevice):
    """
    Класс, представляющий клавиатуру.
    """

    def __init__(self, brand: str, model: str, wireless: bool, layout: str) -> None:
        """
        Инициализирует клавиатуру.

        :param brand: Бренд клавиатуры.
        :param model: Модель клавиатуры.
        :param wireless: Флаг беспроводного соединения.
        :param layout: Раскладка клавиатуры (например, QWERTY, AZERTY).
        """
        super().__init__(brand, model, wireless)
        self.layout = layout

    def __str__(self) -> str:
        """
        Перегруженный метод для отображения информации о клавиатуре.
        """
        return f"{self.brand} {self.model} ({'Wireless' if self.wireless else 'Wired'}) - {self.layout} layout"

    def type_key(self, key: str) -> str:
        """
        Симулирует нажатие клавиши на клавиатуре.

        :param key: Символ или название клавиши.
        :return: Строка, обозначающая нажатие клавиши.
        """
        return f"Нажата клавиша: {key}"


class Mouse(InputDevice):
    """
    Класс, представляющий мышь.
    """

    def __init__(self, brand: str, model: str, wireless: bool, dpi: int) -> None:
        """
        Инициализирует мышь.

        :param brand: Бренд мыши.
        :param model: Модель мыши.
        :param wireless: Флаг беспроводного соединения.
        :param dpi: Разрешение сенсора (DPI).
        """
        super().__init__(brand, model, wireless)
        self.dpi = dpi

    def __str__(self) -> str:
        """
        Перегруженный метод для отображения информации о мыши.
        """
        return f"{self.brand} {self.model} ({'Wireless' if self.wireless else 'Wired'}) - {self.dpi} DPI"

    def change_dpi(self, new_dpi: int) -> str:
        """
        Изменяет значение DPI у мыши.

        :param new_dpi: Новое значение DPI.
        :return: Подтверждение изменения DPI.
        """
        self.dpi = new_dpi
        return f"Разрешение DPI изменено на {self.dpi}"


if __name__ == "__main__":
    keyboard = Keyboard("Logitech", "MX Keys", True, "QWERTY")
    mouse = Mouse("Razer", "DeathAdder", False, 1600)

    print(keyboard)  # Logitech MX Keys (Wireless) - QWERTY layout
    print(mouse)  # Razer DeathAdder (Wired) - 1600 DPI

    print(keyboard.type_key("Enter"))  # Нажата клавиша: Enter
    print(mouse.change_dpi(3200))  # Разрешение DPI изменено на 3200
