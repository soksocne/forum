# Generated by Django 4.0.3 on 2022-03-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
