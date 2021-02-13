# Generated by Django 3.1.5 on 2021-01-24 13:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0006_auto_20210124_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutus', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='aboutus',
        ),
    ]