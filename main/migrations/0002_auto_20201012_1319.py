# Generated by Django 3.1.2 on 2020-10-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='planted_date',
            field=models.DateField(),
        ),
    ]
