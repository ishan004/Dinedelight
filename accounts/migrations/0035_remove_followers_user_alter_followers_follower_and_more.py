# Generated by Django 4.2.6 on 2023-12-05 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0034_alter_followers_follower_alter_followers_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followers",
            name="user",
        ),
        migrations.AlterField(
            model_name="followers",
            name="follower",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 5, 21, 55, 10, 484714)
            ),
        ),
    ]
