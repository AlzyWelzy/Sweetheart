# Generated by Django 4.2.7 on 2024-01-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_crushresponse_proposal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proposal",
            name="response",
            field=models.CharField(
                choices=[("True", "Yes"), ("False", "No")], max_length=5
            ),
        ),
    ]