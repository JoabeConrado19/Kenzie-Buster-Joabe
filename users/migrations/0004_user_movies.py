# Generated by Django 4.1.7 on 2023-02-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_rename_user_movie"),
        ("users", "0003_alter_user_is_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="movies",
            field=models.ManyToManyField(related_name="user", to="movies.movie"),
        ),
    ]