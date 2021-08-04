# Generated by Django 3.1.4 on 2021-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('mail', models.CharField(max_length=250)),
                ('quary', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
