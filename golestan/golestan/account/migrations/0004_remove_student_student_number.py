# Generated by Django 4.0.7 on 2023-11-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_educationalassistant_educational_assistant_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_number',
        ),
    ]