# Generated by Django 3.1.1 on 2020-09-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0006_auto_20200921_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='prop',
            name='cost',
            field=models.IntegerField(default=100),
        ),
    ]
