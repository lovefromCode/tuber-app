from django.db import models
from datetime import datetime

# Create your models here.


class Contact_tuber(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.full_name
