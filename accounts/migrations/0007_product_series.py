# Generated by Django 4.2.3 on 2023-08-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_product_category_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='series',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
