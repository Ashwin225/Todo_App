from django.db import models

# Create your models here.

class TaskStatus(models.Model):
    name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=100)
    
    def get_status_color(self):
        if self.name == 'In Progress':
            return 'green' 

    def __str__(self):
        return self.name
