# Generated by Django 5.0.1 on 2024-01-23 00:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="document",
            field=models.IntegerField(unique=True),
            preserve_default=False,
        ),
    ]
