# Generated by Django 3.1.13 on 2021-09-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210921_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age',
            field=models.CharField(max_length=100),
        ),
    ]
