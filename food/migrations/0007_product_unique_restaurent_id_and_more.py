# Generated by Django 4.1.1 on 2022-09-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_orders_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unique_restaurent_id',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='restaurent',
            name='unique_product_id',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='food/static/img/products'),
        ),
        migrations.AlterField(
            model_name='restaurent',
            name='image',
            field=models.ImageField(default='', upload_to='food/static/img/restaurents'),
        ),
    ]
