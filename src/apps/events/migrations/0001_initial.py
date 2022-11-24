# Generated by Django 4.1.3 on 2022-11-24 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("start", models.DateTimeField()),
                ("finish", models.DateTimeField()),
                ("link_to_stream", models.URLField(blank=True, null=True)),
                ("image", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Prize",
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
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("owner", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="events.event",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="prize",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="events.prize",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="winner",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="event_winner",
                to="events.ticket",
            ),
        ),
        migrations.AddConstraint(
            model_name="event",
            constraint=models.CheckConstraint(
                check=models.Q(("start__lt", models.F("finish"))),
                name="correct_event_datetime",
            ),
        ),
    ]
