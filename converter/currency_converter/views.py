from decimal import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from currency_converter.core.convert_func import convert1
from currency_converter.core.validate import currency_normalize
from currency_converter.core.exceptions import RequestException
# Create your views here.


def convert(request):
    try:
        from_cur = currency_normalize(request.GET.get('from'))
        to_cur = currency_normalize(request.GET.get('to'))
        if (from_cur is None) or (to_cur is None):
            return HttpResponse(content="wrong currency name", status=400)
        required_value = Decimal(request.GET.get('value'))
        result= convert1(from_currency=from_cur, to_currency=to_cur, value=int(required_value), service=None)
        return JsonResponse({'result':result})
    except InvalidOperation:
        return HttpResponse(content="wrong value",status=400)
    except RequestException as exception:
        return HttpResponse(content=f"{exception.message}", status=400)
    except:
        return HttpResponse(status=500)
