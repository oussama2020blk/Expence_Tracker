# Generated by Django 5.1.3 on 2024-12-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_requestloggs'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestloggs',
            name='request_method',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
