# Generated by Django 4.1.7 on 2023-04-03 08:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("case", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["created_time"]},
        ),
    ]
