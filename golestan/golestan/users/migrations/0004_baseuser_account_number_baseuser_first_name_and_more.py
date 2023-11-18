# Generated by Django 4.0.7 on 2023-11-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_baseuser_birth_date_baseuser_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='account_number',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True, verbose_name='account number'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='last name'),
        ),
    ]
