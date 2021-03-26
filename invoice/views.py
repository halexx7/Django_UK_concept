import datetime
import random
import json

from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize


from .models import Payer, Invoice

def main(request):

    payer = serialize('json', Payer.objects.all())
    invoice = serialize('json', Invoice.objects.all())
   

    # payer = {
    #     "period": 'Январь 2021',
    #     "name": 'ИВАНОВ ИВАН ИВАНОВИЧ',
    #     "address": 'ул.Свободы, д.56, к.11',
    #     "square": 80.20,
    #     "num_resident": 5,
    #     "uk": 'ООО "УК Жилищный стандарт", ул.Комсомольская, д.57, тел.:688-085;688-084, ИНН 7202225426 р/с 40702810538320000181 БИК 046577964 к/с 301018101000000000964 Филиал "Екатеринбургский" ОАО "Альфа-Банк"',
    #     "personal_account": 407890098
    # }

    # payer_json = json.dumps(payer_test)

    # payer_items = serialize('json', payer, fields=['period', 'name', 'address', 'square', 'num_resident', 'uk', 'personal_account'])
    return render(request, "invoice/main.html", context={'data': invoice})