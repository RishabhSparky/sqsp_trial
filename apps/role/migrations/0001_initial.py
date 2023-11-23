# Generated by Django 4.2.5 on 2023-09-20 10:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessRole",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("role_permissions", models.JSONField(default=dict)),
                (
                    "company_id",
                    models.UUIDField(
                        blank=True,
                        default=uuid.uuid4,
                        editable=False,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Access Role",
                "verbose_name_plural": "Access Roles",
                "ordering": ["-created_at"],
            },
        ),
    ]
