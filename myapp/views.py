from django.shortcuts import render, redirect
from .models import Status, TodoList
from .forms import TodoListForm
# Create your views here.

def create_item(request):
    todo = TodoList.objects.all()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form = TodoListForm()
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'index.html', context)


def delete_item(request, id):
    todo = TodoList.objects.get(id=id)
    todo.delete()
    return redirect('index')