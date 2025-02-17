# Generated by Django 5.0.7 on 2024-08-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
