# Generated by Django 4.0.4 on 2022-06-10 18:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_blogmodel_body_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='Body',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
