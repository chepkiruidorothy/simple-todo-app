from django.shortcuts import render, redirect
from .models import TodoItem

# Create your views here.

def home(request):
    todo = TodoItem.objects.all()
    return render(request, 'home.html', { 'todo_list': todo })

def add(request):
    title = request.POST["title"]
    todo = TodoItem.objects.create(title=title)
    todo.save()
    return redirect("home")

# def update(request, todo_id):
#     todo = TodoItem.objects.get(id=todo_id)
#     title = request.POST["title"]
#     todo.title = TodoItem.objects.create(title=title)
#     todo.save(update_fields=['title'])
#     return redirect("home")

def delete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect("home")
