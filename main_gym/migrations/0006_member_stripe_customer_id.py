# Generated by Django 4.2 on 2023-05-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_gym', '0005_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
