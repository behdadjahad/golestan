# Generated by Django 4.0.7 on 2023-11-18 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalassistant',
            name='educational_assistant_number',
        ),
        migrations.RemoveField(
            model_name='itmanager',
            name='itmanager_number',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='professor_number',
        ),
    ]
