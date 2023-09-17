import requests
import re
from decimal import *


from .exceptions import RequestException


def get_currency_rate(from_currency, to_currency, service=None):
    """
    Запрос курса валют выполняется с помощью внешнего сервиса
    Реализован только один сервис apilayer
    :param from_currency: код валюты из которой конвертируем
    :param to_currency: код валюты в которую конвертируем
    :param service: наименование используемого сервиса. По умолчанию используется apilayer
    :return: значение курса валюты
    :exeptions: RequestException - при ошибке сервиса или неправильном задании сервиса
    """
    if service is None:
        service = "apilayer"

    if service == "apilayer":
        url = 'https://api.apilayer.com/fixer/latest'
        headers = {'apikey': 'QD5AV13Y04xB6Uz7NANSkADIeGGTgejA'}
        payload ={'base': from_currency, 'symbols': to_currency}
        response = requests.get(url, params=payload, headers=headers)
        response_json = response.json()
        if response_json['success'] == True:
            rate = exstract_rate(response.text, to_currency)
            return rate
        raise RequestException("error to call external converter service apilayer")
    raise RequestException("wrong service name")


def exstract_rate(json_string, currency):
    """

    Выделение курса валюты с помощью конвертации в json ответа сервиса неправильно и приводит к неверному результату.
    Используем регулярные выражения для поиска значения с курсом в строке
    :param json_string: источник информаци о курсе валюты
    :param currency: код валюты курс которой необходимо извлеч
    :return: курс валюты

    """
    pattern = ".{1}%s.{1}\:\D+(\d+(\.\d+)?)" %currency
    result = re.findall(pattern, json_string)
    result1 = result[0]
    return Decimal(result1[0])



if __name__ == '__main__':
    print(get_currency_rate(from_currency='USD', to_currency='RUB'))
    print(type(get_currency_rate(from_currency='USD', to_currency='RUB')))
#get_currency_rate(from_currency='USD', to_currency=1)