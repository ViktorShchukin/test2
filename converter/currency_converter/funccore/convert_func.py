from .request_for_currency import get_currency_rate


def do_convert(from_currency, to_currency, value, service=None):
    """
    Конвертирует валюту
    :param from_currency: код валюты из которой конвертируем
    :param to_currency: код валюты в которую конвертируем
    :param value: конвертируемое значение
    :param service: наименование используемого сервиса
    :return: конвертированное значение
    """
    result = get_currency_rate(from_currency, to_currency, service)
    converted = value * result
    return converted

if __name__ == '__main__':
    do_convert('USD','RUB',2)