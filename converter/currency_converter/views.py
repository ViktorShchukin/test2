from decimal import *


from django.http import HttpResponse, JsonResponse


from .funccore import do_convert, currency_normalize, RequestException
from .oopcore import get_converter_holder
# Create your views here.


def oop_convert(request):
    try:
        from_cur = currency_normalize(request.GET.get('from'))
        to_cur = currency_normalize(request.GET.get('to'))
        if (from_cur is None) or (to_cur is None):
            return HttpResponse(content="wrong currency name", status=400)
        required_value = Decimal(request.GET.get('value', ''))
        result = get_converter_holder().converter_by_name("apilayer").convert(from_cur, to_cur, required_value)
        return JsonResponse({'result': result, 'currency': to_cur})
    except InvalidOperation:
        return HttpResponse(content="wrong value", status=400)
    except RequestException as exception:
        return HttpResponse(content=f"{exception.message}", status=400)
    except:
        return HttpResponse(status=500)


def func_convert(request):
    try:
        from_cur = currency_normalize(request.GET.get('from'))
        to_cur = currency_normalize(request.GET.get('to'))
        if (from_cur is None) or (to_cur is None):
            return HttpResponse(content="wrong currency name", status=400)
        required_value = Decimal(request.GET.get('value'))
        result = do_convert(from_currency=from_cur, to_currency=to_cur, value=int(required_value), service=None)
        return JsonResponse({'result': result, 'currency': to_cur})
    except InvalidOperation:
        return HttpResponse(content="wrong value", status=400)
    except RequestException as exception:
        return HttpResponse(content=f"{exception.message}", status=400)
    except:
        return HttpResponse(status=500)
