# Generated by Django 3.0.11 on 2020-12-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201208_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(null=True),
        ),
    ]
