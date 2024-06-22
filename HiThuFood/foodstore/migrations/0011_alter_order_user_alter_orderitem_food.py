# Generated by Django 5.0.6 on 2024-06-15 07:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0010_rename_toppings_order_item_topping_topping_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodstore.food'),
        ),
    ]