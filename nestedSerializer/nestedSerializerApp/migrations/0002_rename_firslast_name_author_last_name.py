# Generated by Django 3.2.9 on 2021-11-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nestedSerializerApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firslast_name',
            new_name='last_name',
        ),
    ]