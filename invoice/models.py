from django.db import models

class  invoice(models.Model):
    person_account = models.CharField(verbose_name="person_account", max_length=32, unique=True)
    period = models.DateField(verbose_name="period")

    def __str__(self):
        return self.person_account