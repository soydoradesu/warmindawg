# Generated by Django 5.1.1 on 2024-09-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
