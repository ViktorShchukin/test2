import requests
from decimal import *
from currency_converter.core.exceptions import RequestException
def request(from_currency, to_currency, service=None):
    if service is None:
        service = "apilayer"

    if service == "apilayer":
        url = 'https://api.apilayer.com/fixer/latest'
        headers = {'apikey': 'QD5AV13Y04xB6Uz7NANSkADIeGGTgejA'}
        payload ={'base': from_currency, 'symbols': to_currency}
        response = requests.get(url, params=payload, headers=headers)
        response_json = response.json()
        if response_json['success'] == True:
            currency = response_json['rates']
            return Decimal(currency[to_currency])
        raise RequestException("error to call external converter service apilayer")

if __name__ == '__main__':
    request(from_currency='USD', to_currency='RUB')
    request(from_currency='USD', to_currency=1)