from .converterapilayer import ConverterAPILayer


class ConverterHolder:
    """
    Класс интерфейс для доступа к конвертерам
    """
    def __init__(self):
        self.converters = {"apilayer": ConverterAPILayer()}

    def converter_by_name(self, name: str):
        result = self.converters[name]
        if result is None:
            result = self.converters["apilayer"]
        return result
