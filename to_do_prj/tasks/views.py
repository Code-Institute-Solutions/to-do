from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Task
from .forms import TaskForm


def get_tasks(request):
    """A view that displays all tasks"""
    all_tasks = Task.objects.all()
    return render(request, 'tasks.html', {'task_list': all_tasks})


def task_detail(request, id):
    """A view that displays the details of a specific task"""
    task = get_object_or_404(Task, pk=id)
    return render(request, "taskdetail.html", {'task': task})


def add_task(request):
    """A view that handles the form for adding a new task"""
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect(task_detail, task.pk)
    else:
        form = TaskForm()

    return render(request, 'taskform.html', {'form': form})


def edit_task(request, id):
    """A view that handles the form for editing an existing task"""
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect(task_detail, task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskform.html', {'form': form})


def toggle_status(request, id):
    """A view that toggles the value of a task's Done field"""
    task = get_object_or_404(Task, pk=id)
    task.done = not task.done
    task.save()
    return redirect(get_tasks)
