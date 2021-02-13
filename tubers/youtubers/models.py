from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.


class Youtuber(models.Model):

    crew_choice = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )

    camera_choice = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('fuji', 'fuji'),
        ('red', 'red'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    )

    category_choice = (
        ('code', 'code'),
        ('tech_review', 'tech_review'),
        ('vlogs', 'vlogs'),
        ('comedy', 'comedy'),
        ('gaming', 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
    )
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtuber/%Y/%m')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choice, max_length=255)
    camera_type = models.CharField(choices=camera_choice, max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choice, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
