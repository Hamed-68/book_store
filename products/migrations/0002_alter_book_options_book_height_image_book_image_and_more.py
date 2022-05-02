# Generated by Django 4.0 on 2022-04-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='book',
            name='height_image',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, height_field=models.PositiveIntegerField(default=50), upload_to='images', verbose_name='تصویر', width_field=models.PositiveIntegerField(default=50)),
        ),
        migrations.AddField(
            model_name='book',
            name='width_image',
            field=models.PositiveIntegerField(default=50),
        ),
    ]