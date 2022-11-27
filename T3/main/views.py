from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main site page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create_ticket(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_ticket.html', context)

def thanks_page(request):
    return render(request, 'main/thanks_page.html')