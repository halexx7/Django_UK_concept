# Generated by Django 2.2.17 on 2021-03-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_remove_invoice_person_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice'),
        ),
    ]
