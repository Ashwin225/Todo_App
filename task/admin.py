from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=('name','description','category','image','status','time_to_do')
# Register your models here.
admin.site.register(Task,TaskAdmin)