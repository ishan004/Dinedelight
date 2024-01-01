# Generated by Django 4.2.6 on 2023-12-05 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0029_alter_post_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followers",
            name="follower",
        ),
        migrations.RemoveField(
            model_name="followers",
            name="user",
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 5, 21, 8, 24, 944860)
            ),
        ),
    ]