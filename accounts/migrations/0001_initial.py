# Generated by Django 3.2 on 2021-06-07 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address_first', models.TextField()),
                ('address', models.TextField()),
                ('restaurant_latitude', models.FloatField(null=True)),
                ('restaurant_longitude', models.FloatField(null=True)),
                ('mobile', models.IntegerField()),
                ('orders', models.IntegerField(default=0)),
                ('total_sale', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'PENDING '), (1, 'TO_BE_VERIFY'), (2, 'APPROVED')], default=0)),
                ('restaurant_name', models.CharField(max_length=100)),
                ('serving_type_food', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('fssai_number', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('address_first', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('orders', models.IntegerField(default=0)),
                ('total_sale', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, 'PENDING '), (1, 'TO_BE_VERIFY'), (2, 'APPROVED')], default=0)),
                ('restaurant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('serving_type_food', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('fssai_number', models.CharField(blank=True, max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=100, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('login_as', models.IntegerField(blank=True, choices=[(0, 'RESTAURANT OWNER '), (1, 'CUSTOMER')], null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdetail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
