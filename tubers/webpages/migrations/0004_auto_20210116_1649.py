# Generated by Django 3.1.5 on 2021-01-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(max_length=255),
        ),
    ]
