# Generated by Django 4.2.5 on 2023-09-21 11:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("role", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessrole",
            name="company_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, null=True
            ),
        ),
    ]
