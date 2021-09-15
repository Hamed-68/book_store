# Generated by Django 3.2.6 on 2021-09-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='name',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
    ]
