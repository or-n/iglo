# Generated by Django 3.2.7 on 2021-11-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0008_alter_game_points_difference'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
