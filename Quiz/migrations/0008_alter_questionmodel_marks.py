# Generated by Django 4.0.4 on 2022-06-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_alter_questionmodel_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionmodel',
            name='Marks',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
