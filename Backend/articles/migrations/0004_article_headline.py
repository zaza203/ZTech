# Generated by Django 5.0.4 on 2024-04-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
