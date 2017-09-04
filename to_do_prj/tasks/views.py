from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def get_tasks(request):
    return render(request, 'tasks.html', {'task_list': Task.objects.all()})
 
def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)
    task.save()
    return render(request, "taskdetail.html", {'task': task})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(task_detail, task.pk)
    else:
        form = TaskForm()
    return render(request, 'taskform.html', {'form': form})


def edit_task(request, id):
   task = get_object_or_404(Task, pk=id)
   if request.method == "POST":
       form = TaskForm(request.POST, request.FILES, instance=task)
       if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(task_detail, task.pk)
   else:
       form = TaskForm(instance=task)
   return render(request, 'taskform.html', {'form': form})