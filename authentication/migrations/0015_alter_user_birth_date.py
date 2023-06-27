# Generated by Django 4.2.2 on 2023-06-24 04:26

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0014_alter_user_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                null=True, validators=[authentication.models.check_date]
            ),
        ),
    ]