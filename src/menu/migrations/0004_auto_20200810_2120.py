# Generated by Django 3.0.8 on 2020-08-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_sandwich_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='image',
            field=models.ImageField(blank=True, upload_to='front_end/src/assets'),
        ),
    ]