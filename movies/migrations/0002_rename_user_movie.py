# Generated by Django 4.1.7 on 2023-02-23 20:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Movie",
        ),
    ]
