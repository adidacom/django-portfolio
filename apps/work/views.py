from django.shortcuts import render, HttpResponse, redirect
from .models import Work
# Create your views here.


def index(request):
    context = {
        'projects': Work.objects.all().order_by('-created_at')
    }

    return render(request, 'work/index.html', context)
