# Generated by Django 3.1.2 on 2020-10-08 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apiTest', '0005_auto_20201008_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
