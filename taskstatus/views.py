from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def taskstatus_list(request):
    taskstatus = TaskStatus.objects.all()
    return render(request, 'taskstatus_list.html', {'taskstatus': taskstatus})
 

