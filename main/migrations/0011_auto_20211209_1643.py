# Generated by Django 3.2.9 on 2021-12-09 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211208_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=255, verbose_name='Прізвище')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Адреса')),
                ('status', models.CharField(choices=[('completed', 'Замовлення виконано'), ('new', 'Нове замовлення'), ('is_ready', 'Замовлення готове'), ('in_progress', 'Замовлення в розробці')], default='new', max_length=100, verbose_name='Статус замовлення')),
                ('buying_type', models.CharField(choices=[('self', 'Самовівиз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип замовлення')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Коментар до замовлення')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата створення замовлення')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата отримання замовлення')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='main.customer', verbose_name='Покупець')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='main.Order', verbose_name='Замовлення покупця'),
        ),
    ]
