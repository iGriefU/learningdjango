# Generated by Django 2.1.5 on 2020-04-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]
