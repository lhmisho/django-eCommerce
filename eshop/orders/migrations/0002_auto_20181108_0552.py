# Generated by Django 2.0 on 2018-11-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'CREATED'), ('paid', 'PAID'), ('shipped', 'SHIPPING'), ('refounded', 'REFOUNDED')], default='created', max_length=120),
        ),
    ]
