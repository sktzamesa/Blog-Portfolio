# Generated by Django 5.0.7 on 2024-10-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0018_alter_about_options_rename_date_about_date_of_birth_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="about",
            old_name="postal_code",
            new_name="zip_code",
        ),
        migrations.AddField(
            model_name="about",
            name="photo",
            field=models.ImageField(blank=True, upload_to="user/%Y/%m/%d"),
        ),
    ]
