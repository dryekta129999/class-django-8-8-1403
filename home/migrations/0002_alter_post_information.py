# Generated by Django 5.1.4 on 2024-12-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="information",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
