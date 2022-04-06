
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('task/create', views.taskCreate, name="taskcreate"),
    path('task/update/<int:pk>', views.taskUpdate, name="taskupdate")
]