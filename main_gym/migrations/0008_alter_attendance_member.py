# Generated by Django 4.1.2 on 2023-05-04 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_gym', '0007_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_gym.member'),
        ),
    ]