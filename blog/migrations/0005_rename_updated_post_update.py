# Generated by Django 5.0.4 on 2024-07-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_update_post_updated_alter_post_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="updated",
            new_name="update",
        ),
    ]
