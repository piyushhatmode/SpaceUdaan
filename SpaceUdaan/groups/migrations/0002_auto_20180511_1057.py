# Generated by Django 2.0.2 on 2018-05-11 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='decription',
            new_name='description',
        ),
    ]