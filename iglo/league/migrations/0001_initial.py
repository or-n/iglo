# Generated by Django 3.2.7 on 2021-10-28 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import league.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('promotion_count', models.SmallIntegerField()),
                ('players_per_group', models.SmallIntegerField()),
                ('state', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='league.group')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=32, unique=True)),
                ('rank', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(null=True)),
                ('order', models.SmallIntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='league.group')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='league.player')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='group',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='league.season'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win_type', models.CharField(choices=[('points', 'Punkty'), ('resign', 'Rezygnacja'), ('time', 'Czas')], max_length=8, null=True)),
                ('points_difference', models.SmallIntegerField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('server', models.CharField(choices=[('OGS', 'OGS'), ('KGS', 'KGS')], max_length=3)),
                ('link', models.URLField(null=True)),
                ('sgf', models.FileField(null=True, upload_to=league.models.game_upload_to)),
                ('black', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_black', to='league.member')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='league.group')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='league.round')),
                ('white', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_as_white', to='league.member')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_games', to='league.member')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('server', models.CharField(choices=[('OGS', 'OGS'), ('KGS', 'KGS')], max_length=3)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.player')),
            ],
        ),
    ]
