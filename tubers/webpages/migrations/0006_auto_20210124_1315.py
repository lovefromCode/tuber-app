# Generated by Django 3.1.5 on 2021-01-24 13:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_about'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AddField(
            model_name='team',
            name='aboutus',
            field=ckeditor.fields.RichTextField(default='something about the project.'),
        ),
    ]
