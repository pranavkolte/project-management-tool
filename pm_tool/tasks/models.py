import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Tasks(models.Model):
    STATUS_CHOICES = (
        ('To Do', 'To Do'), 
        ('In Progress', 'In Progress'), 
        ('Done', 'Done'), 
    )
    PRIORITY_CHOICES = (
        ('Low', 'Low'), 
        ('Medium', 'Medium'), 
        ('High', 'High'), 
    )
    
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TimeField(null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, null=False)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False)
    

class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    