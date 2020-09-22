# Generated by Django 3.1.1 on 2020-09-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='site_photos')),
                ('vastu', models.CharField(max_length=50)),
                ('facilities', models.CharField(max_length=50)),
            ],
        ),
    ]
