from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'blog/homepage.html')


def about(request):
    return render(request, 'blog/aboutpage.html')
