from currency_converter.core.request_for_currency import request


def convert1(from_currency, to_currency, value, service=None):
    result = request(from_currency, to_currency, service)
    converted = value * result
    return converted

if __name__ == '__main__':
    convert('USD','RUB',2)