import datetime
import invoice
import random
from django.http import JsonResponse
import simplejson as json

from django.conf import settings
from django.contrib.postgres import fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize

from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView


from .models import UK, Invoice, House, Street, City, Appartament, User


def main(request):

    invoice = serialize('json', User.objects.prefetch_related().all())

    return render(request, "invoice/main.html", context={'data': invoice})
    # return render(request, "invoice/main.html", context={})

class InvoiceViews(ListView):
    context_object_name = 'invoice'
    template_name = 'invoice/main.html'
    queryset = serialize('json', User.objects.prefetch_related().all())

    def get_context_data(self, **kwargs):
        context = super(InvoiceViews, self).get_context_data(**kwargs)
        context['appartaments'] = serialize('json', Appartament.objects.prefetch_related().all())
        context['house'] = serialize('json', House.objects.prefetch_related().all())
        context['city'] = serialize('json', City.objects.prefetch_related().all())
        context['street'] = serialize('json', Street.objects.prefetch_related().all())
        context['uk'] = serialize('json', UK.objects.prefetch_related().all())
        context['invoice'] = serialize('json', Invoice.objects.all().prefetch_related().all())
        return context




