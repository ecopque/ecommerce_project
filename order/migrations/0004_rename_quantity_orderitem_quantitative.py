# Generated by Django 5.1.1 on 2024-10-25 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantity',
            new_name='quantitative',
        ),
    ]
