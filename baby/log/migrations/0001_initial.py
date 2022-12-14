# Generated by Django 3.2.14 on 2022-08-02 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.PositiveIntegerField(help_text='Введите мл', verbose_name='Сколько мл')),
                ('pub_date', models.DateTimeField(verbose_name='Дата записи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['-pub_date'],
            },
        ),
    ]
