# Generated by Django 3.2.14 on 2022-08-17 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SLeepTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date_start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата записи')),
                ('pub_date_end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата записи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sleeptime', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Время сна',
                'verbose_name_plural': 'Время сна',
                'ordering': ['-pub_date_start'],
            },
        ),
    ]