# Generated by Django 3.0.8 on 2020-08-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200810_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]