# Generated by Django 3.1.2 on 2020-10-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTest', '0003_auto_20201008_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
