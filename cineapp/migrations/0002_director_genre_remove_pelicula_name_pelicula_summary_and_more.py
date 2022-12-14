# Generated by Django 4.1.1 on 2022-09-20 13:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cineapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Director",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                (
                    "date_of_dead",
                    models.DateField(blank=True, null=True, verbose_name="Died"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                (
                    "name",
                    models.CharField(help_text="Genero de la pelicula", max_length=64),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="pelicula",
            name="name",
        ),
        migrations.AddField(
            model_name="pelicula",
            name="summary",
            field=models.TextField(
                default=datetime.datetime(
                    2022, 9, 20, 13, 26, 46, 539828, tzinfo=datetime.timezone.utc
                ),
                help_text="Resumen de la pelicula",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pelicula",
            name="title",
            field=models.CharField(default=-1.0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pelicula",
            name="director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="cineapp.director",
            ),
        ),
        migrations.AddField(
            model_name="pelicula",
            name="genre",
            field=models.ManyToManyField(to="cineapp.genre"),
        ),
    ]
