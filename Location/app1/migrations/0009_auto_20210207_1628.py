# Generated by Django 3.0.4 on 2021-02-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20210207_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Pincode',
            field=models.IntegerField(blank=True, max_length=5, verbose_name='zipcode'),
        ),
    ]
