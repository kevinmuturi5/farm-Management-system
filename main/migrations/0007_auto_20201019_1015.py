# Generated by Django 3.1.2 on 2020-10-19 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_labourer_allproj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labourer',
            name='allproj',
        ),
        migrations.AlterField(
            model_name='labourer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='labouror', to=settings.AUTH_USER_MODEL),
        ),
    ]