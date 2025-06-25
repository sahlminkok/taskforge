from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    context = { 'tasks': tasks }
    return render(request, 'tasks/index.html', context)

def detail(request, pk):
    task = Task.objects.get(id=pk)
    context = { 'task': task }
    return render(request, 'tasks/detail.html', context)
