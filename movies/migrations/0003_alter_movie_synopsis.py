# Generated by Django 4.1.7 on 2023-02-24 01:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_rename_user_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]