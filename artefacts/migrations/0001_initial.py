# Generated by Django 4.0.4 on 2022-06-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artefact",
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
                ("title", models.CharField(max_length=256)),
                ("country", models.CharField(max_length=128, null=True)),
                ("description", models.CharField(max_length=512, null=True)),
            ],
        ),
    ]
