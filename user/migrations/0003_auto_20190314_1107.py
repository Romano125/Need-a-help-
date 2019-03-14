# Generated by Django 2.1.5 on 2019-03-14 10:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_auto_20190314_1057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobRate',
            new_name='Rate',
        ),
        migrations.RemoveField(
            model_name='requestrate',
            name='repairman',
        ),
        migrations.RemoveField(
            model_name='requestrate',
            name='request',
        ),
        migrations.DeleteModel(
            name='RequestRate',
        ),
    ]
