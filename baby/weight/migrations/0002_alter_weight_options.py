# Generated by Django 3.2.14 on 2022-08-14 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Вес', 'verbose_name_plural': 'Вес'},
        ),
    ]