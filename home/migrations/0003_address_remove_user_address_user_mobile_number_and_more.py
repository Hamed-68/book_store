# Generated by Django 4.0 on 2022-04-23 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210910_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200, verbose_name='استان')),
                ('city', models.CharField(max_length=200, verbose_name='شهر')),
                ('area', models.CharField(blank=True, max_length=200, verbose_name='منطقه')),
                ('street', models.CharField(max_length=200, verbose_name='خیابان')),
                ('alley', models.CharField(blank=True, max_length=200, verbose_name='کوچه')),
                ('plaque', models.CharField(blank=True, max_length=200, verbose_name='پلاک')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(default=' ', max_length=11, verbose_name='موبایل'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=' ', max_length=11, verbose_name='تلفن'),
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
    ]