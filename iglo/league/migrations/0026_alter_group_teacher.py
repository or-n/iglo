# Generated by Django 3.2.9 on 2022-02-23 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20220123_1539'),
        ('league', '0025_alter_player_egd_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='review.teacher'),
        ),
    ]
