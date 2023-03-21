from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'blog/homepage.html', {'title': 'Main page Site', 'tasks': tasks})


def about(request):
    return render(request, 'blog/aboutpage.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Incorect form"
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', context)