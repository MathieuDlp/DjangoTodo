from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from .models import Task
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    
    if request.method == "POST":
        newTask = Task()
        newTask.title = request.POST["title"]
        newTask.save()

    tasks = Task.objects.all()
    
    context = ({"tasks": tasks})

    # template = loader.get_template("todo/home.html")
    # request_context = RequestContext(request)
    # request_context.push(context)
    # return HttpResponse(template.render(context))
    return render(request, "todo/home.html", context)


#optional other create task form
def taskCreate(request):
    if request.method == "POST":
        newTask = Task()
        newTask.title = request.POST["title"]
        if newTask.is_valid():
            newTask.save()
    template = loader.get_template("todo/task_create_form.html")
    return HttpResponse(template.render(request))

def taskUpdate(request, pk):
    
    actual_task = Task.objects.get(id=pk)
    print(actual_task.title)
    if request.method == "POST":
        actual_task.title = request.POST["title"]
        # actual_task.completed = request.POST["completed"]
        actual_task.save()
        # return reverse_lazy("index")
        return redirect("index")

    return render(request, "todo/task_update_form.html")