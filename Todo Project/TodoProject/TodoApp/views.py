from django.shortcuts import render, redirect # type: ignore
from .models import Todo
from .form import TodoFrom

# Create your views here.
def form_view(request):
    success_message = ""
    if request.method == 'POST':
        form = TodoFrom(request.POST)
        if form.is_valid(): 
            task = request.POST.get('task')
            description = request.POST.get('description')
            status = request.POST.get('status')
            # Create a new Todo instance and save it to the database
            Todo.objects.create(task=task, description=description, status=status)
            # Set the success message
            success_message = "Todo added successfully!"
    
    return render(request, 'form.html', {'success_message': success_message})
def todo(request):

    todos = Todo.objects.all()
    return render(request, 'todo.html', {'todos': todos})

def Edit(request, pk):
    success_message = ""
    todo_obj = Todo.objects.get(id=pk)
    data = {'todo': todo_obj}
    if request.method == 'POST':
        form = TodoFrom(request.POST)
        if form.is_valid(): 
            task = request.POST.get('task')
            description = request.POST.get('description')
            status = request.POST.get('status')
            todo_obj.task = task
            todo_obj.description = description
            todo_obj.status = status
            todo_obj.save()
            data['success_message'] = "Todo Edited successfully!"
    return render(request, 'Edit.html', context=data)



def Delete(request, pk):
        todo_obj = Todo.objects.get(id=pk)
        todo_obj.delete()
        return redirect('Todo')

def Delete_All(request):
    Todo.objects.all().delete()
    return redirect('Todo')
