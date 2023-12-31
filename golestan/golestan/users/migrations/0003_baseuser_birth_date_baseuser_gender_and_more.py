# Generated by Django 4.0.7 on 2023-11-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='birth date'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='national_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='national id'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='phone number'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
