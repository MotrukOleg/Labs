# Generated by Django 5.1.2 on 2024-11-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premier_django', '0007_standings_games_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
