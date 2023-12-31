# Generated by Django 4.0.7 on 2023-11-18 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100, null=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('units', models.IntegerField()),
                ('course_type', models.CharField(choices=[('general', 'Genaral'), ('specialized', 'Specialized'), ('basic', 'Basic'), ('theorical', 'Theorical'), ('practical', 'Practical')], max_length=100)),
                ('co_requisites', models.ManyToManyField(blank=True, null=True, related_name='corequisites', to='faculty.approvedcourse')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
                ('pre_requisites', models.ManyToManyField(blank=True, null=True, related_name='prerequisites', to='faculty.approvedcourse')),
            ],
        ),
    ]
