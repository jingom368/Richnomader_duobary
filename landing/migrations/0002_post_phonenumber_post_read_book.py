# Generated by Django 4.0.4 on 2022-05-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phonenumber',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='read_book',
            field=models.TextField(null=True),
        ),
    ]
