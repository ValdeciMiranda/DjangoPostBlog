# Generated by Django 5.0 on 2023-12-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="title_tag",
            field=models.CharField(default="PostBlog", max_length=255),
        ),
    ]
