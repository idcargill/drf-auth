# Generated by Django 4.0.3 on 2022-03-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duckmodel',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]