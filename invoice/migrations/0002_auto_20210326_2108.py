# Generated by Django 2.2.17 on 2021-03-26 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('add_number', models.PositiveIntegerField(verbose_name='add_number')),
                ('sq_appart', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='sq_appart')),
                ('num_owner', models.PositiveIntegerField(default=0, verbose_name='num_owner')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128, verbose_name='city')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128, verbose_name='street')),
            ],
        ),
        migrations.CreateModel(
            name='TypeServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('unit', models.CharField(max_length=128, verbose_name='unit')),
                ('standard', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='standard')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='standard')),
            ],
        ),
        migrations.CreateModel(
            name='UK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='services')),
                ('requisites', models.TextField(verbose_name='requisites')),
                ('web_addr', models.CharField(max_length=128, verbose_name='services')),
            ],
        ),
        migrations.RemoveField(
            model_name='payer',
            name='num_resident',
        ),
        migrations.RemoveField(
            model_name='payer',
            name='uk',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_account', models.CharField(max_length=32, unique=True, verbose_name='person_account')),
                ('name', models.CharField(max_length=128, verbose_name='services')),
                ('appartament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Appartament')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('add_number', models.PositiveIntegerField(verbose_name='number')),
                ('sq_home', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='sq_home')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.City')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.Street')),
                ('uk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.UK')),
            ],
        ),
        migrations.AddField(
            model_name='appartament',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.House'),
        ),
    ]
