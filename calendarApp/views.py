from django.shortcuts import render
from .models import Entry


def index(request):
    entries = Entry.objects.all()
    return render(request, 'calendarApp/index.html', {'entries': entries})


def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'calendarApp/details.html', {'entry': entry})
