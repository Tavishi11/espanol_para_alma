# Generated by Django 3.1.4 on 2021-07-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20210712_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.TextField(max_length=1000),
        ),
    ]
