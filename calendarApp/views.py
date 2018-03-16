from django.shortcuts import render
from .models import Entry


def index(request):
    entries = Entry.objects.all()
    return render(request, 'calendarApp/index.html', {'entries': entries})
