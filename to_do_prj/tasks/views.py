from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'index.html')

    
def get_tasks(request):
    return render(request, 'tasks.html', {'task_list': Task.objects.all()})

 
def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)
    task.save()
    return render(request, "taskdetail.html", {'task': task})


def add_task(request):
    """A view that handles the form for adding a new task 
    
    any interesting logic
    """
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            #single line comment
            #even if it overflows
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


def update_status(request, id):
    status = request.POST['status']
    task = Task.objects.get(id=id)
    task.status = "Done"
    task.save()
    return redirect(reverse('get_tasks'))        
   


