# Generated by Django 3.2.9 on 2021-12-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211208_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Розмір'),
        ),
    ]
