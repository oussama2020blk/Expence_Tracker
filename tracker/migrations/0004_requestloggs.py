# Generated by Django 5.1.3 on 2024-12-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_trackinghistory_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLoggs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_info', models.TextField()),
                ('request_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]