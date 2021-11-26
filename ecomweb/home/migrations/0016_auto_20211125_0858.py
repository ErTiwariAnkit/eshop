# Generated by Django 3.2.8 on 2021-11-25 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211125_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal',
            field=models.IntegerField(default=0),
        ),
    ]
