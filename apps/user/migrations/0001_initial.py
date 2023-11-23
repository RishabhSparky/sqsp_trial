# Generated by Django 4.2.5 on 2023-09-20 10:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("role", "__first__"),
        ("company", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
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
                ("full_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("password", models.CharField(max_length=255, null=True)),
                (
                    "designation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_super_user", models.BooleanField(default=False)),
                ("is_company_owner", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="company.company",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="role.accessrole",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
                "unique_together": {("role", "email")},
            },
        ),
    ]
