# Generated by Django 3.2.8 on 2021-11-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_otp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal',
            field=models.IntegerField(),
        ),
    ]
