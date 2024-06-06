# Generated by Django 5.0.5 on 2024-05-30 06:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Members",
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
                ("username", models.CharField(max_length=50)),
                ("userEmail", models.CharField(max_length=100)),
                ("userPassword", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "members",
            },
        ),
    ]