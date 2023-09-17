import re
from decimal import *
import requests


from .converter import Converter
from .exception import RequestException

url = 'https://api.apilayer.com/fixer/latest'
headers = {'apikey': 'QD5AV13Y04xB6Uz7NANSkADIeGGTgejA'}


class ConverterAPILayer(Converter):
    """
    Класс реализующий конвертацию валюты с помощью сервиса apilayer
    """
    def __init__(self):
        pass

    def convert(self, cur_code_from, cur_code_to, value):
        """
        Конвертирует валюту
        :param cur_code_from: код валюты из которой конвертируем
        :param cur_code_to: код валюты в которую конвертируем
        :param value: конвертируемое значение
        :return: конвертированное значение
        """
        payload = {'base': cur_code_from, 'symbols': cur_code_to}
        response = requests.get(url, params=payload, headers=headers)
        response_json = response.json()
        if response_json['success'] is True:
            rate = self.extract_rate(response.text, cur_code_to)
            return rate * value
        raise RequestException("error to call external converter service apilayer")

    def extract_rate(self, json_string: str, currency: str):
        """
        Выделение курса валюты с помощью конвертации в json ответа сервиса неправильно
        и приводит к неверному результату.
        Используем регулярные выражения для поиска значения с курсом в строке
        :param json_string: источник информаци о курсе валюты
        :param currency: код валюты курс которой необходимо извлеч
        :return: курс валюты
        """
        pattern = ".{1}%s.{1}\:\D+(\d+(\.\d+)?)" % currency
        result = re.findall(pattern, json_string)
        result1 = result[0]
        return Decimal(result1[0])
