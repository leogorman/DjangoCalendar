from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryForm


def index(request):
    return render(request, 'calendarApp/index.html')


def calendar(request):
    entries = Entry.objects.all()
    return render(request, 'calendarApp/calendar.html', {'entries': entries})


def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'calendarApp/details.html', {'entry': entry})


def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description,
            ).save()

            return HttpResponseRedirect('/')
    else:
        form = EntryForm()

    return render(request, 'calendarApp/form.html', {'form': form})


def delete(request, pk):

    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, id=pk)
        entry.delete()

    return HttpResponseRedirect('/')


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
