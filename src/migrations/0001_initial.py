# Generated by Django 4.2.3 on 2023-07-22 03:23

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
            name='GymBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('open', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blacklist', to=settings.AUTH_USER_MODEL)),
                ('id_reglamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.regulation')),
            ],
        ),
        migrations.CreateModel(
            name='Assistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
