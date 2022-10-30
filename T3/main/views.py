from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main site page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create_ticket(request):
    return render(request, 'main/create_ticket.html')