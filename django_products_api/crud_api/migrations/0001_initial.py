# Generated by Django 4.1.1 on 2022-09-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('product_image', models.ImageField(default=None, upload_to='')),
                ('manufacturer', models.CharField(max_length=100)),
                ('date_listed', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
