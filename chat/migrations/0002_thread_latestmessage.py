# Generated by Django 2.1.3 on 2019-05-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='latestMessage',
            field=models.TextField(default=''),
        ),
    ]