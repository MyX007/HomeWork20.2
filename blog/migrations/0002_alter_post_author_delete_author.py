# Generated by Django 5.0.7 on 2024-08-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
