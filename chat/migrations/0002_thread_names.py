# Generated by Django 2.1.3 on 2019-06-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='names',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
