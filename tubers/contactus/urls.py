from django.urls import path
from . import views

urlpatterns = [
    path('contact_tuber', views.contact_tuber, name="contact_tuber"),
]
