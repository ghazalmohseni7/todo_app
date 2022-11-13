from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
from django.views.generic import ListView
from django.urls import reverse


# Create your views here.

class list_todo_items(ListView):
    model = Todo
    template_name = 'templates/todo/todo_list.html'
    todoList = Todo.objects.all()
    context = {'todo_list': todoList}


# def list_todo_items(request):
#     todoList = Todo.objects.all()
#     context = {'todo_list': todoList}
#     return render(request, 'todos/todo_list.html',context)


def insert_todo_item(request):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect(reverse('list_todo'))


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect(reverse('list_todo'))
