# Generated by Django 5.1.4 on 2024-12-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
