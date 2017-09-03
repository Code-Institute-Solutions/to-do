from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def get_tasks(request):
    return render(request, 'tasks.html', {'task_list': Task.objects.all()})
    
def add_task(request):
    if request.method == "POST":
        new = Task()
        new.name = request.POST.get('name')
        new.description = request.POST.get('description')
        new.status = request.POST.get('status')

        new.save()

        return render(request, 'tasks.html', {'task_list': Task.objects.all()})
    else:
        return render(request, 'add_task.html')
