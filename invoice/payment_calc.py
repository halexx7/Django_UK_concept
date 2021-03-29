from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView


from .models import UK, Invoice, House, Street, City, Appartament, User

def payment_calc():
    services = Invoice.objects.all()
    services = list(services)

    
