from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    tasks = request.user.tasks.all()
    context = { 'tasks': tasks }
    return render(request, 'tasks/index.html', context)

def detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('users:login')

    task = get_object_or_404(Task, id=pk, user=request.user)
    context = { 'task': task }
    return render(request, 'tasks/detail.html', context)

def create_task(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()

    context = { 'form': form }
    return render(request, 'tasks/create_task.html', context)

def update_task(request, pk):
    if not request.user.is_authenticated:
        return redirect('users:login')

    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:detail', pk=task.id)
    else:
        form = TaskForm(instance=task)

    context = { 'form': form }
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    if not request.user.is_authenticated:
        return redirect('users:login')
    
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')

    context = { 'task': task }
    return render(request, 'tasks/delete_confirmation.html', context)
