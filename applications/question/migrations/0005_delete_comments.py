# Generated by Django 4.0.3 on 2022-03-27 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_comments_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
