# Generated by Django 4.2.2 on 2023-06-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0013_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]
