# Generated by Django 3.0.7 on 2021-07-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_auto_20210712_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='paying',
            field=models.ManyToManyField(blank=True, default=0, to='project.Course'),
        ),
    ]
