# Generated by Django 4.2.6 on 2023-11-28 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_user_profile_location_alter_post_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 29, 0, 26, 41, 193001)
            ),
        ),
        migrations.AlterField(
            model_name="user_profile",
            name="profile_image",
            field=models.ImageField(
                default="/media/profile_image/blank-profile-picture.png",
                upload_to="profile_image/",
            ),
        ),
    ]
