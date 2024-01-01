# Generated by Django 4.2.6 on 2023-12-05 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0020_alter_followers_follower_alter_followers_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followers",
            name="follower",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="followers",
            name="user",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 5, 17, 52, 2, 883534)
            ),
        ),
    ]