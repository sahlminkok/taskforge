from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    context = { 'tasks': tasks }
    return render(request, 'tasks/index.html', context)

def detail(request, pk):
    task = Task.objects.get(id=pk)
    context = { 'task': task }
    return render(request, 'tasks/detail.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    context = { 'form': form }
    return render(request, 'tasks/create_task.html', context)

def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=task.id)
    else:
        form = TaskForm(instance=task)

    context = { 'form': form }
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    context = { 'task': task }
    return render(request, 'tasks/delete_confirmation.html', context)
