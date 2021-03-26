from django.db import models
from django.contrib.postgres.fields import JSONField

class Payer(models.Model):
    person_account = models.CharField(verbose_name="person_account", max_length=32, unique=True)
    period = models.CharField(verbose_name="period", max_length=128)
    name = models.CharField(verbose_name="services", max_length=128)
    address = models.CharField(verbose_name="address", max_length=128)
    square = models.DecimalField(verbose_name="square", max_digits=5, decimal_places=2, default=0)
    num_resident = models.PositiveIntegerField(verbose_name="num_resident", default=0)
    uk = models.CharField(verbose_name="uk", max_length=512)

    def __str__(self):
        return self.person_account


class Invoice(models.Model):
    person_account = models.CharField(verbose_name="person_account", max_length=32, unique=True)
    period = models.DateField(verbose_name="period")
    data = JSONField(verbose_name="payer")

    def __str__(self):
        return self.person_account

