# Generated by Django 4.2.6 on 2023-11-28 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_user_profile_bio_alter_post_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 28, 22, 57, 24, 133830)
            ),
        ),
    ]
