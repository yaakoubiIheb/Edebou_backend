# Generated by Django 4.0.3 on 2022-04-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(default='issue', max_length=100),
        ),
    ]
