# Generated by Django 4.1.7 on 2023-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyTable",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("filename", models.CharField(max_length=255)),
                ("result", models.BooleanField()),
            ],
        ),
    ]
