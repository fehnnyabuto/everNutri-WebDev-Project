# Generated by Django 4.2.7 on 2023-11-28 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_cartitem_delete_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
