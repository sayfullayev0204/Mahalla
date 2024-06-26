# Generated by Django 5.0.4 on 2024-05-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adduser", "0051_alter_certificate_overel_alter_certificate_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="title",
            field=models.CharField(
                choices=[
                    ("english", "english"),
                    ("others", "others"),
                    ("nemesis", "nemesis"),
                ],
                max_length=300,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="title",
            field=models.CharField(
                choices=[
                    ("english", "english"),
                    ("others", "others"),
                    ("nemesis", "nemesis"),
                ],
                max_length=300,
                verbose_name="Language",
            ),
        ),
    ]
