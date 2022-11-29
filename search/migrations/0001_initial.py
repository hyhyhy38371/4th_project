# Generated by Django 4.1.3 on 2022-11-28 19:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Beer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("big_kind", models.CharField(max_length=100)),
                ("kind", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("brewery", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=100)),
                ("abv", models.CharField(max_length=100)),
                ("average", models.CharField(max_length=100)),
                ("ratings", models.CharField(max_length=100)),
                ("reviews", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("body", models.FloatField()),
                ("sweet", models.FloatField()),
                ("fruity", models.FloatField()),
                ("hoppy", models.FloatField()),
                ("malty", models.FloatField()),
                ("like_count", models.PositiveIntegerField(default=0)),
                (
                    "like_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_beers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
