# Generated by Django 5.0.1 on 2024-01-22 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0003_alter_bill_products'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='bills', through='bills.BillProduct', to='products.product'),
        ),
    ]