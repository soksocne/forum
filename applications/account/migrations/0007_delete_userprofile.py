# Generated by Django 4.0.3 on 2022-03-29 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_userprofile_age_alter_userprofile_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
