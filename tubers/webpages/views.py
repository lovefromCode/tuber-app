from django.shortcuts import render, get_object_or_404
from . import models
from youtubers.models import Youtuber


def home(request):
    slider = models.Slider.objects.all()
    teams = models.Team.objects.all()
    youtuber = Youtuber.objects.order_by(
        '-created_at').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_at').all()

    data = {
        'slider': slider,
        'teams': teams,
        'youtuber': youtuber,
        'all_tubers': all_tubers,
    }
    return render(request, 'webpages/home.html', data)


def youtuber_details(request, id):
    # tuber = Youtuber.objects.get(id=id)
    tuber = get_object_or_404(Youtuber, pk=id)
    data = {
        'tuber': tuber
    }
    return render(request, 'youtubers/youtuber_details.html', data)


def about(request):
    teams = models.Team.objects.all()
    aboutus = models.About.objects.all()

    data = {
        'teams': teams,
        'aboutus': aboutus,
    }
    return render(request, 'webpages/about.html', data)



def contact(request):
    return render(request, 'webpages/contact.html')
