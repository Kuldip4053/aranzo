# Generated by Django 5.0.7 on 2024-07-26 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_cupan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cupan',
            old_name='cupan',
            new_name='c_code',
        ),
    ]
