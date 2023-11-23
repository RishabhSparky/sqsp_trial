# Generated by Django 4.2.5 on 2023-09-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="invite_type",
            field=models.CharField(
                choices=[
                    ("Internal", "INTERNAL"),
                    ("Company", "COMPANY"),
                    ("Company Owner", "COMPANY OWNER"),
                ],
                default="Company Owner",
                max_length=20,
            ),
        ),
    ]
