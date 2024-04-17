# Generated by Django 5.0.4 on 2024-04-16 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0014_actors_gender_remove_movie_actors_movie_actors"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dressing_Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("floor", models.IntegerField()),
                ("number", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="actors",
            name="dressing",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="movie_app.dressing_room",
            ),
        ),
    ]
