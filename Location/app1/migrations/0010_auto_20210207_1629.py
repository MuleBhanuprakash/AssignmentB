# Generated by Django 3.0.4 on 2021-02-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20210207_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Pincode',
            field=models.IntegerField(blank=True, verbose_name='zipcode'),
        ),
    ]
