# Generated by Django 5.0.5 on 2024-06-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.CharField(max_length=50)),
                ("purpose", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "contact",
            },
        ),
    ]