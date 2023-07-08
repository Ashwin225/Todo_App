from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('user_form/',views.user_form,name='user_insert'),
    path('<int:id>/',views.user_form,name='user_update'),
    path('user_list/',views.user_list,name='user_list'),
    path('tasks/',views.tasks,name='tasks'),
    path('user_delete/<int:id>/',views.user_delete,name='user_delete'),
    path('todo_section/',views.todo_section,name='todo_section'),
    path('mail/',views.mail,name='mail'),
]