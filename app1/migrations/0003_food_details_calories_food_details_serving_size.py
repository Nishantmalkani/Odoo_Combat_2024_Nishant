# Generated by Django 5.0.6 on 2024-06-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_remove_food_details_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="food_details",
            name="calories",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="food_details",
            name="serving_size",
            field=models.IntegerField(default=0),
        ),
    ]
