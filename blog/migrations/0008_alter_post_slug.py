# Generated by Django 5.0.7 on 2024-07-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
