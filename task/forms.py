from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    
    class Meta:
        model = Task
        fields = ('name','description','category','image','status','time_to_do')
        labels =  {
            'name':('Task Name'),
            'time_to_do':("Date_to_do('YY-MM-DD')"),
        }
         
        def __str__(self):
            return self.name
            
    def __init__(self,*args,**kwargs):
            super(TaskForm,self).__init__(*args,**kwargs)
            self.fields['status'].empty_label = "Select"
            self.fields['name'].required = False
            self.fields['status'].required = False
            self.fields['time_to_do'].required = False
            self.fields['image'].required = False
            self.fields['description'].required = False
            self.fields['category'].required = False


class MailForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    message = forms.CharField(required=False)
