from django.shortcuts import render,redirect,HttpResponse
from .models import Task
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import MailForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

def mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)

        if form.is_valid():
            print("the form is valid")
    else:
          form = MailForm()
    return render(request, 'mail.html', {'form' :form})


# Create your views here.

def index(request):
    #task=Task.objects.all()
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_insert')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

        
        
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            return redirect('signup',)
            
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()

        return redirect('login')

    return render(request,'signup.html')

def home(request):
    return render(request, 'home.html')


def user_list(request):
     context = {'user_list':Task.objects.all()}
     return render(request, 'user_register/user_list.html',context)

def user_form(request,id=0):
    
    if request.method == "GET":
      
      if id == 0:
         form = TaskForm()
         
      else:
          user = User.objects.get(pk=id)
          form = TaskForm(instance=user)
      return render(request, 'user_register/user_form.html',{'form':form})
    else:
      if id == 0:
        form = TaskForm(request.POST)
        print(request)
      else:
        user = User.objects.get(pk=id)
        form = TaskForm(request.POST,instance=user)
      if form.is_valid():
        form.save()
      else:
          print(form.errors)
      return redirect('user_list')

def user_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('user_list')


def todo_section(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the Task table
    return render(request, 'user_register/todo_section.html', {'tasks': tasks})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})
def user_insert(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_section')
    else:
        form = TaskForm()
    return render(request, 'user_register/user_form.html', {'form': form})

from django.shortcuts import render


def mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        
        
        if form.is_valid():
            name = form.cleaned_data['name']
            message =  form.cleaned_data['message']
            

            html = render_to_string('mailfile/review.html',{
                'name': name,
                'message': message
            })
            send_mail('the review subject','this is the message','noreply@me.com',['inevalker@gmail.com'],html_message = html)
            return redirect('mail')
    else:
          form = MailForm()
    return render(request, 'mailfile/mail.html', {'form' :form})