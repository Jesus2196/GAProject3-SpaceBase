# Generated by Django 3.2.8 on 2021-11-05 18:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SpaceObject',
            new_name='Star',
        ),
        migrations.RenameField(
            model_name='star',
            old_name='so_type',
            new_name='star_type',
        ),
    ]
