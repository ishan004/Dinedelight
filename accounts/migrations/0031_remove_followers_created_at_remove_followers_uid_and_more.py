# Generated by Django 4.2.6 on 2023-12-05 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0030_remove_followers_follower_remove_followers_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followers",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="followers",
            name="uid",
        ),
        migrations.RemoveField(
            model_name="followers",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="followers",
            name="follower",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="followers",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="followers",
            name="user",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 5, 21, 10, 51, 180375)
            ),
        ),
    ]
