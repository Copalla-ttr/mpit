# Generated by Django 5.0 on 2023-12-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(choices=[], max_length=32, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]