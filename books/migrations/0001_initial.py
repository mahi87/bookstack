# Generated by Django 5.0.3 on 2024-03-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                ("book_id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=50)),
                ("publication_year", models.IntegerField()),
                ("genre", models.CharField(max_length=50)),
                ("isbn", models.CharField(max_length=50)),
                ("publisher", models.CharField(max_length=50)),
                ("language", models.CharField(max_length=50)),
                ("num_pages", models.IntegerField()),
                ("price", models.IntegerField()),
                ("summary", models.TextField()),
                ("created_at", models.DateField()),
                (
                    "ownership_type",
                    models.CharField(
                        choices=[
                            ("E-Book", "E Book"),
                            ("Audio Book", "Audio Book"),
                            ("Owned Physical Book", "Owned Physical Copy"),
                            ("Borrowed Book", "Borrowed Book"),
                        ],
                        default="Owned Physical Book",
                        max_length=50,
                    ),
                ),
                ("notes", models.TextField()),
            ],
        ),
    ]