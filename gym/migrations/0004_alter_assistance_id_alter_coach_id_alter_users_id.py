# Generated by Django 4.2.3 on 2023-07-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_alter_assistance_id_alter_coach_id_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
