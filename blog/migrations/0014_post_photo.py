# Generated by Django 5.0.7 on 2024-10-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_trigram_ext"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="photo",
            field=models.ImageField(blank=True, upload_to="user/%Y/%m/%d"),
        ),
    ]
