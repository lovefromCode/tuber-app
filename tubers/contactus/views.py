from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
# Create your views here.


def contact_tuber(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

        contact_tuber = models.Contact_tuber(
            full_name=full_name, phone=phone, email=email, message=message, company_name=company_name, subject=subject)
        contact_tuber.save()
        messages.success(request, 'Thanks for contacting us!')
        return redirect('home')
