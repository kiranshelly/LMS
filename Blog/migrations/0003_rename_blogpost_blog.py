# Generated by Django 4.0.4 on 2022-06-08 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_remove_blogpost_author_remove_blogpost_datetime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Blog',
        ),
    ]
