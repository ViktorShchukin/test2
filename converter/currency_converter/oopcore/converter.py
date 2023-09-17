from decimal import *


class Converter:
    """
    Базовый класс для конвертеров.
    От него наследуются все реализации конвертеров.
    """
    def __init__(self):
        pass

    def convert(self, cur_code_from: str, cur_code_to: str, value: Decimal):
        pass
