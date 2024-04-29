# Generated by Django 4.2.11 on 2024-04-29 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Administrator",
            fields=[
                (
                    "Administrator_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="department",
            fields=[
                (
                    "department_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Docter",
            fields=[
                ("Docter_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("update_time", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(model_name="patient", name="author",),
        migrations.RemoveField(model_name="patient", name="price",),
        migrations.RemoveField(model_name="patient", name="publish_time",),
        migrations.RemoveField(model_name="patient", name="publisher",),
    ]
