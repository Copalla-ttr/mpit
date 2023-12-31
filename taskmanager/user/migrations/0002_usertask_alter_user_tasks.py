# Generated by Django 5.0 on 2023-12-06 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='tasks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertask'),
        ),
    ]
