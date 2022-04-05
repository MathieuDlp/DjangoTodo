from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Task

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
    if request == "POST":
        newTask = Task()
        newTask.title = request.POST["title"]
        if newTask.is_valid():
            newTask.save()
    template = loader.get_template("todo/task_create_form.html")
    return HttpResponse(template.render(request))

def taskUpdate(request, pk):
    if request == "POST":
        actual_task = Task.objects.get(id =pk)

    template = loader.get_template("todo/task_update_form.html")
    return HttpResponse(template.render(request))