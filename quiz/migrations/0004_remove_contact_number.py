# Generated by Django 4.1.5 on 2023-06-06 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_title_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='number',
        ),
    ]
