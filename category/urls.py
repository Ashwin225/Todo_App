from django.urls import path
from . import views


urlpatterns = [
    path('',views.helo,name='helo'),
    
]