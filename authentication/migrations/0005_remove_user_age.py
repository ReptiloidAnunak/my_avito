# Generated by Django 4.2.2 on 2023-06-24 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_alter_user_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="age",
        ),
    ]