# Generated by Django 3.2.7 on 2022-08-31 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_compression', '0002_dwt_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwt_img',
            name='name',
            field=models.CharField(default='Dwt_img_name', max_length=50),
        ),
    ]
