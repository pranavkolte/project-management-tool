import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Projects(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ProjectMember(models.Model):
    ROLE_CHOICES = ( 
        ('Admin', 'Admin'), 
        ('Member', 'Member'), 
    )
    project_member_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Projects, on_delete=models.Case)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    