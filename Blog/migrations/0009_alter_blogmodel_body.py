# Generated by Django 4.0.4 on 2022-06-10 18:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_blogmodel_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='Body',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
