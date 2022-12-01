from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Todo

# Create your views here.
# tasks = ['foo', 'bar', 'baz']


def search(request):
    term = request.GET.get('search') or ''
    tasks = Todo.objects.filter(task__icontains=term)
    context = {'tasks': tasks}
    return render(request, "index.html", context)


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'add.html', {'form': form})


def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(request, 'update.html', {'form': form})


def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('index')
    return render(request, 'index.html', {'task': task})
