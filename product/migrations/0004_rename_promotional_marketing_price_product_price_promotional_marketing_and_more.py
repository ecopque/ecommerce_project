# Generated by Django 5.1.1 on 2024-10-03 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_variation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='promotional_marketing_price',
            new_name='price_promotional_marketing',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='promotional_price',
            new_name='price_promotional',
        ),
    ]
