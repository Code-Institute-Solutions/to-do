from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    all_tasks = Task.objects.all()
    return render(request, 'index.html', {'task': all_tasks})