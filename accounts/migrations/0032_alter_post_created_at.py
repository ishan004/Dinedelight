# Generated by Django 4.2.6 on 2023-12-05 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0031_remove_followers_created_at_remove_followers_uid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 5, 21, 12, 52, 178347)
            ),
        ),
    ]
