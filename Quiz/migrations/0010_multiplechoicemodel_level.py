# Generated by Django 4.0.4 on 2022-06-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0009_multiplechoicemodel_singlechoicemodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicemodel',
            name='Level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
