# Generated by Django 4.2 on 2024-09-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(max_length=35, verbose_name="Телефон"),
        ),
    ]
