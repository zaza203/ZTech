# Generated by Django 5.0.4 on 2024-04-13 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], null=True),
        ),
    ]