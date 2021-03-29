from django.conf import settings
from django.contrib.postgres import fields
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from django.utils.safestring import mark_safe


from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView


from .models import UK, Invoice, House, Street, City, Appartament, User


def main(request):

    invoice = mark_safe(serialize('json', User.objects.filter(pk=1)))
    return render(request, "invoice/main.html", context={'data': invoice})


class InvoiceViews(ListView):
    context_object_name = 'user'
    template_name = 'invoice/main.html'
    # queryset = serialize('json', User.objects.prefetch_related().all())
    queryset = mark_safe(serialize('json', User.objects.filter(pk=1)))

    def get_context_data(self, **kwargs):
        context = super(InvoiceViews, self).get_context_data(**kwargs)
        context['appartaments'] = mark_safe(serialize('json', Appartament.objects.all()))
        context['house'] = mark_safe(serialize('json', House.objects.prefetch_related().all()))
        context['city'] = mark_safe(serialize('json', City.objects.prefetch_related().all()))
        context['street'] = mark_safe(serialize('json', Street.objects.prefetch_related().all()))
        context['uk'] = mark_safe(serialize('json', UK.objects.prefetch_related().all()))
        context['invoice'] = mark_safe(serialize('json', Invoice.objects.all().prefetch_related().all()))
        return context