from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'blog/homepage.html', {'title': 'Main page Site', 'tasks': tasks})


def about(request):
    return render(request, 'blog/aboutpage.html')
