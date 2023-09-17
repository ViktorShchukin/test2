
def currency_normalize(currency):
    """
    Проверяет правильность значений кодов валют
    :param currency: проверяемой код
    :return: проверенный код или None если код неправильный
    """
    if type(currency) is str:
        standart_curency = currency.upper()
        currency_list = ['USD', 'RUB']
        for value in currency_list:
            if value == standart_curency:
                return value
    return None

if __name__ == '__main__':
    res = currency_normalize('USD')
    print(res)
    res = currency_normalize('usd')
    print(res)
    res = currency_normalize('qwe')
    print(res)
    res = currency_normalize(None)
    print(res)