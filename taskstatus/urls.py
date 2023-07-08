from django.urls import path
from . import views


urlpatterns = [
    path('taskstatus_list/',views.taskstatus_list,name='taskstatus_list'),
   
]
