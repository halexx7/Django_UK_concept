from typing import Callable
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.deletion import CASCADE
from django.db.models.lookups import In


class Invoice(models.Model):
    period = models.DateField(verbose_name="period")
    data = JSONField(verbose_name="payer")


class TypeServices(models.Model):
    name = models.CharField(verbose_name="name", max_length=128)
    unit = models.CharField(verbose_name="unit", max_length=128)
    standard = models.DecimalField(verbose_name="standard", max_digits=5, decimal_places=2)
    rate = models.DecimalField(verbose_name="standard", max_digits=6, decimal_places=2)

    class Meta:
        default_related_name = 'Services'

    def __str__(self):
        return self.name


class City(models.Model):
    city = models.CharField(verbose_name="city", max_length=128)

    class Meta:
        default_related_name = 'city'

    def __str__(self):
        return self.city


class Street(models.Model):
    street = models.CharField(verbose_name="street", max_length=128)

    class Meta:
        default_related_name = 'street'

    def __str__(self):
        return self.street



class UK(models.Model):
    name = models.CharField(verbose_name="services", max_length=128)
    requisites = models.TextField(verbose_name="requisites")
    web_addr = models.CharField(verbose_name="services", max_length=128)

    class Meta:
        default_related_name = 'uk'

    def __str__(self):
        return self.name

class House(models.Model):
    number = models.PositiveIntegerField(verbose_name="number")
    add_number = models.PositiveIntegerField(verbose_name="number")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    sq_home = models.DecimalField(verbose_name="sq_home", max_digits=5, decimal_places=2)
    uk = models.ForeignKey(UK, on_delete=CASCADE)

    class Meta:
        default_related_name = 'house'

    def __str__(self):
        return self.street

class Appartament(models.Model):
    house = models.ForeignKey(House, on_delete=CASCADE)
    number = models.PositiveIntegerField(verbose_name="number")
    add_number = models.PositiveIntegerField(verbose_name="add_number")
    sq_appart = models.DecimalField(verbose_name="sq_appart", max_digits=5, decimal_places=2)
    num_owner = models.PositiveIntegerField(verbose_name="num_owner", default=0)

    class Meta:
        default_related_name = 'appartament'


class User(models.Model):
    personal_account = models.CharField(verbose_name="personal_account", max_length=32, unique=True)
    name = models.CharField(verbose_name="user_name", max_length=128)
    appartament = models.ForeignKey(Appartament, on_delete=CASCADE, default=1)
    invoice = models.ForeignKey(Invoice, on_delete=CASCADE, default=1)

    class Meta:
        default_related_name = 'user'
