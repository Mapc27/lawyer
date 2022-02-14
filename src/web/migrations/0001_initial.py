# Generated by Django 4.0.2 on 2022-02-14 06:23

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolvedApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=100)),
                ('history', models.TextField()),
                ('result', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number incorrect', regex='^(\\+7|8|)([0-9]{10})$')])),
                ('person_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_notified', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('phone_number', 'person_name', 'description')},
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('is_staff', models.BooleanField(default=False)),
                ('telegram_user_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Telegram user ID')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', web.models.UserManager()),
            ],
        ),
    ]
