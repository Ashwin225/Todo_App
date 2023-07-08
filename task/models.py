from django.db import models
from category.models import Category
from taskstatus.models import TaskStatus
from datetime import datetime



CATEGORY_CHOICES = (
    ( 'Important','Important'),
    ('Urgent','Urgent'),
    ('Not Important','Not Important'),

)

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50,choices= CATEGORY_CHOICES, default='Not Important')
    image = models.ImageField(upload_to='task/templates/images/')
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    time_to_do=models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['status']