# Generated by Django 5.0.6 on 2024-06-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0015_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]