# Generated by Django 4.1.6 on 2023-03-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TeleBotSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telegram_token",
                    models.CharField(max_length=200, verbose_name="Telegram token"),
                ),
                (
                    "telegram_chat_id",
                    models.CharField(max_length=200, verbose_name="Telegram chat id"),
                ),
                ("telegram_message", models.TextField(verbose_name="Layout message")),
            ],
            options={
                "verbose_name": "Настройку",
                "verbose_name_plural": "Настройки",
            },
        ),
    ]
