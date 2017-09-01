from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def get_tasks(request):
    return render(request, 'tasks.html', {'task_list': Task.objects.all()})