# Generated by Django 3.0.7 on 2021-07-21 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_auto_20210721_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='paying',
            field=models.ManyToManyField(blank=True, default=0, null=True, to='project.Course'),
        ),
    ]
