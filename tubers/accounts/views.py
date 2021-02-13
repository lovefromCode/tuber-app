from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from youtubers import models
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid credential')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            # If username and email are already in database
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username already exits")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email already exits")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Account created Successfully.')
                return redirect("login")
        else:
            messages.warning(request, 'Password do not match.')
            return redirect("register")

    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect("/")


@login_required(login_url='login')
def dashboard(request):
    youtuber = models.Youtuber.objects.order_by('id').all()

    data = {
        'youtuber': youtuber
    }
    return render(request, 'accounts/dashboard.html', data)
