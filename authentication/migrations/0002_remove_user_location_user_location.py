# Generated by Django 4.2.2 on 2023-06-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="location",
        ),
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.ManyToManyField(to="authentication.location"),
        ),
    ]
