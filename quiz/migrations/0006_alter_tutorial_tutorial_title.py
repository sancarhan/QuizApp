# Generated by Django 4.1.5 on 2023-05-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_Title',
            field=models.CharField(max_length=20000),
        ),
    ]
