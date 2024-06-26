# Generated by Django 5.0.3 on 2024-03-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="ownership_type",
            field=models.CharField(
                choices=[
                    ("E-Book", "E Book"),
                    ("Audio Book", "Audio Book"),
                    ("Owned Physical Book", "Owned Physical Book"),
                    ("Borrowed Book", "Borrowed Book"),
                ],
                default="Owned Physical Book",
                max_length=50,
            ),
        ),
    ]
