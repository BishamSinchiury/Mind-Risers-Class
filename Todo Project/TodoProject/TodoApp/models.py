from django.db import models #type: ignore

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=50)
    description = models.TextField()
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('Not Done', 'Not Done'),
        ('In Progress', 'In Progress'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_done')
    